import time
from urllib.parse import urlencode

import requests

from pipedrive import exceptions
from pipedrive.activities import Activities
from pipedrive.deals import Deals
from pipedrive.filters import Filters
from pipedrive.notes import Notes
from pipedrive.organizations import Organizations
from pipedrive.persons import Persons
from pipedrive.pipelines import Pipelines
from pipedrive.products import Products
from pipedrive.recents import Recents
from pipedrive.stages import Stages
from pipedrive.users import Users
from pipedrive.webhooks import Webhooks


class Client:
    BASE_URL = 'https://api-proxy.pipedrive.com/'
    OAUTH_BASE_URL = 'https://oauth.pipedrive.com/oauth/'

    def __init__(self, client_id=None, client_secret=None, domain=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.api_token = None
        self.activities = Activities(self)
        self.deals = Deals(self)
        self.filters = Filters(self)
        self.notes = Notes(self)
        self.organizations = Organizations(self)
        self.persons = Persons(self)
        self.pipelines = Pipelines(self)
        self.products = Products(self)
        self.recents = Recents(self)
        self.stages = Stages(self)
        self.users = Users(self)
        self.webhooks = Webhooks(self)

        if domain:
            if not domain.endswith('/'):
                domain += '/'
            self.BASE_URL = domain + 'v1/'

    def authorization_url(self, redirect_uri, state=None):
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
        }

        if state is not None:
            params['state'] = state

        return self.OAUTH_BASE_URL + 'authorize?' + urlencode(params)

    def exchange_code(self, redirect_uri, code):
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        return self._post(self.OAUTH_BASE_URL + 'token', data=data, auth=(self.client_id, self.client_secret))

    def refresh_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        }
        return self._post(self.OAUTH_BASE_URL + 'token', data=data, auth=(self.client_id, self.client_secret))

    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_api_token(self, api_token):
        self.api_token = api_token

    def _get(self, url, params=None, **kwargs):
        return self._request('get', url, params=params, **kwargs)

    def _get_all(self, url, params=None, **kwargs):
        more = True
        start = 0
        final_response = {}
        data = []
        while more:
            if not params:
                params = {"start": start}
            else:
                params['start'] = start
            response = {}
            try:
                response = self._get(url, params, **kwargs)
            except exceptions.BaseError:
                # If something is already in final_response, return that, otherwise return the response.
                if final_response:
                    return final_response
                return response

            try:
                data.extend(response['data'])
                final_response = response
                final_response['data'] = data
            except KeyError:    # No 'data' key found
                if final_response:
                    return final_response
                return response

            try:
                if response['additional_data']['pagination']['more_items_in_collection']:
                    start = response['additional_data']['pagination']['next_start']
                else:
                    more = False
            except KeyError:
                more = False

        return final_response

    def _post(self, url, **kwargs):
        return self._request('post', url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request('put', url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('delete', url, **kwargs)

    def _request(self, method, url, headers=None, params=None, **kwargs):
        _headers = {}
        _params = {}
        if self.access_token:
            _headers['Authorization'] = 'Bearer {}'.format(self.access_token)
        if self.api_token:
            _params['api_token'] = self.api_token
        if headers:
            _headers.update(headers)
        if params:
            _params.update(params)

        if 'number_of_retries' in kwargs:
            number_of_retries = kwargs.get('number_of_retries', 0)
            intervaltime = kwargs.get('intervaltime', 500)
            del kwargs['number_of_retries']

            if 'intervaltime' in kwargs:
                del kwargs['intervaltime']

            while number_of_retries > 0:
                try:
                    response = self._parse(requests.request(method, url, headers=_headers, params=_params, **kwargs))
                    # No except, response is ok, return it.
                    return response
                except (exceptions.BadRequestError, exceptions.UnauthorizedError, exceptions.NotFoundError,
                        exceptions.UnsupportedMediaTypeError, exceptions.UnprocessableEntityError,
                        exceptions.NotImplementedError, exceptions.TooManyRequestsError):
                    # Do not retry, just return the response.
                    return response
                except (exceptions.ForbiddenError, exceptions.InternalServerError, exceptions.ServiceUnavailableError,
                        exceptions.UnknownError) as e:
                    # Retry! There is hope.
                    number_of_retries -= 1
                    time.sleep(intervaltime / 1000.0)
        else:
            return self._parse(requests.request(method, url, headers=_headers, params=_params, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'Content-Type' in response.headers and 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            return response.text

        if not response.ok:
            error = None
            if 'error' in r:
                error = r['error']
            if status_code == 400:
                raise exceptions.BadRequestError(error, response)
            elif status_code == 401:
                raise exceptions.UnauthorizedError(error, response)
            elif status_code == 403:
                raise exceptions.ForbiddenError(error, response)
            elif status_code == 404:
                raise exceptions.NotFoundError(error, response)
            elif status_code == 410:
                raise exceptions.GoneError(error, response)
            elif status_code == 415:
                raise exceptions.UnsupportedMediaTypeError(error, response)
            elif status_code == 422:
                raise exceptions.UnprocessableEntityError(error, response)
            elif status_code == 429:
                raise exceptions.TooManyRequestsError(error, response)
            elif status_code == 500:
                raise exceptions.InternalServerError(error, response)
            elif status_code == 501:
                raise exceptions.NotImplementedError(error, response)
            elif status_code == 503:
                raise exceptions.ServiceUnavailableError(error, response)
            else:
                raise exceptions.UnknownError(error, response)

        return r
