import requests
from urllib.parse import urlencode, urlparse, quote_plus
from base64 import b64encode


class Client:
    flow_base_url = "https://oauth.pipedrive.com/oauth/"
    oauth_end = "authorize?"
    token_end = "token"
    api_base_url = ""
    example_url = "https://api-proxy.pipedrive.com"
    header = {"Accept": "application/json, */*", "content-type": "application/json"}

    def __init__(self, client_id=None, client_secret=None, token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

    def make_request(self, method, endpoint, data=None, json=None, **kwargs):
        """
            this method do the request petition, receive the different methods (post, delete, patch, get) that the api allow
            :param method:
            :param endpoint:
            :param data:
            :param kwargs:
            :return:
        """
        if self.token:
            self.header["Authorization"] = "Bearer " + self.token
            url = '{0}{1}'.format(self.api_base_url, endpoint)

            if method == "get":
                response = requests.request(method, url, headers=self.header, params=kwargs)
            else:
                response = requests.request(method, url, headers=self.header, data=data, json=json)
            return self.parse_response(response)
        else:
            raise Exception("To make petitions the token is necessary")

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request('get', endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('post', endpoint, data=data, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request('delete', endpoint, **kwargs)

    def _patch(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('patch', endpoint, data=data, json=json, **kwargs)

    def _put(self, endpoint, json=None, **kwargs):
        return self.make_request('put', endpoint, json=json, **kwargs)

    def parse_response(self, response):
        """
            This method get the response request and returns json data or raise exceptions
            :param response:
            :return:
        """
        if response.status_code == 204 or response.status_code == 201:
            return True
        elif response.status_code == 400:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check your request body and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 401:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 403:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 404:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 410:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 422:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 429:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 500:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 501:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        return response.json()

    def get_oauth_uri(self, redirect_uri, state=None):
        if redirect_uri is not None:
            params = {
                'client_id': self.client_id,
                'redirect_uri': redirect_uri,
                # 'scope': ' '.join(scope),
            }
            if state is not None:
                params['state'] = state
            url = self.flow_base_url + self.oauth_end + urlencode(params)
            print(url)
            return url
        else:
            raise Exception("The attributes necessary to get the url were not obtained.")

    def exchange_code(self, redirect_uri, code):
        if redirect_uri is not None and code is not None:
            url = self.flow_base_url + self.token_end
            authorization = '{0}:{1}'.format(self.client_id, self.client_secret)
            header = {'Authorization': 'Basic {0}'.format(b64encode(authorization.encode('UTF-8')).decode('UTF-8'))}
            args = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirect_uri}
            response = requests.post(url, headers=header, data=args)
            return self.parse_response(response)
        else:
            raise Exception("The attributes necessary to exchange the code were not obtained.")

    def refresh_token(self, refresh_token):
        if refresh_token is not None:
            url = self.flow_base_url + self.token_end
            data = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': "refresh_token",
                'refresh_token': refresh_token,
            }
            response = requests.post(url, data=data)
            return self.parse_response(response)
        else:
            raise Exception("The attributes necessary to refresh the token were not obtained.")

    def set_token(self, token):
        """
            Sets the Token for its use in this library.
            :param token:
            :return:
        """
        if token:
            self.token = token

    def get_deals(self, **kwargs):
        url = "{0}/deals".format(self.api_base_url)
        return self._get(url, **kwargs)

    def create_deal(self, **kwargs):
        url = "{0}/deals".format(self.api_base_url)
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def duplicate_deal(self, deal_id):
        if deal_id is not None:
            url = "{0}/deals/{1}/duplicate".format(self.api_base_url, deal_id)
            return self._post(url)
