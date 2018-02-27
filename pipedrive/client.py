import requests
from urllib.parse import urlencode, urlparse, quote_plus
from base64 import b64encode


class Client:
    flow_base_url = "https://oauth.pipedrive.com/oauth/"
    oauth_end = "authorize?"
    token_end = "token"
    api_version = "v1/"
    header = {"Accept": "application/json, */*", "content-type": "application/json"}

    def __init__(self, api_base_url, client_id=None, client_secret=None, oauth=False):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth = oauth
        self.api_base_url = api_base_url
        self.token = None

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
            if self.oauth:
                self.header["Authorization"] = "Bearer " + self.token
                url = '{0}{1}{2}'.format(self.api_base_url, self.api_version, endpoint)
            else:
                url = '{0}{1}{2}?api_token={3}'.format(self.api_base_url, self.api_version, endpoint, self.token)
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

    def get_recent_changes(self, **kwargs):
        """
            This method Returns data about all recent changes occured after given timestamp. in kwarg must to send "since_timestamp" with this format: YYYY-MM-DD HH:MM:SS
            :param kwargs:
            :return:
        """
        if kwargs is not None:
            url = "recents"
            return self._get(url, **kwargs)

    def get_data(self, endpoint, **kwargs):
        if endpoint != "":
            return self._get(endpoint, **kwargs)

    def get_specific_data(self, endpoint, data_id, **kwargs):
        if endpoint != "":
            url = "{0}/{1}".format(endpoint, data_id)
            return self._get(url, **kwargs)

    def create_data(self, endpoint, **kwargs):
        if endpoint != "" and kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(endpoint, json=params)

    # Deals section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Deals
    def get_deals(self, deal_id=None, **kwargs):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
        else:
            url = "deals"
        return self._get(url, **kwargs)

    def create_deal(self, **kwargs):
        url = "deals"
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_deal(self, deal_id, **kwargs):
        if deal_id is not None and kwargs is not None:
            url = "deals/{0}".format(deal_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_deal(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
            return self._delete(url)

    def duplicate_deal(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}/duplicate".format(deal_id)
            return self._post(url)

    def get_deal_details(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
            return self._get(url)

    def get_deals_by_name(self, **kwargs):
        if kwargs is not None:
            url = "deals/find"
            return self._get(url, **kwargs)

    def get_deal_followers(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}/followers".format(deal_id)
            return self._get(url)

    def add_follower_to_deal(self, deal_id, user_id):
        if deal_id is not None and user_id is not None:
            url = "deals/{0}/followers".format(deal_id)
            return self._post(url, json=user_id)

    def delete_follower_to_deal(self, deal_id, follower_id):
        if deal_id is not None and follower_id is not None:
            url = "deals/{0}/followers/{1}".format(deal_id, follower_id)
            return self._delete(url)

    def get_deal_participants(self, deal_id, **kwargs):
        if deal_id is not None:
            url = "deals/{0}/participants".format(deal_id)
            return self._get(url, **kwargs)

    def add_participants_to_deal(self, deal_id, person_id):
        if deal_id is not None and person_id is not None:
            url = "deals/{0}/participants".format(deal_id)
            return self._post(url, json=person_id)

    def delete_participant_to_deal(self, deal_id, participant_id):
        if deal_id is not None and participant_id is not None:
            url = "deals/{0}/participants/{1}".format(deal_id, participant_id)
            return self._delete(url)

    def get_deal_activities(self, deal_id, **kwargs):
        if deal_id is not None:
            url = "deals/{0}/activities".format(deal_id)
            return self._get(url, **kwargs)

    def get_deal_mail_messages(self, deal_id, **kwargs):
        if deal_id is not None:
            url = "deals/{0}/mailMessages".format(deal_id)
            return self._get(url, **kwargs)

    def get_deal_products(self, deal_id, **kwargs):
        if deal_id is not None:
            url = "deals/{0}/products".format(deal_id)
            return self._get(url, **kwargs)

    # Notes section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Notes
    def get_notes(self, note_id=None, **kwargs):
        if note_id is not None:
            url = "notes/{0}".format(note_id)
        else:
            url = "notes"
        return self._get(url, **kwargs)

    def create_note(self, **kwargs):
        if kwargs is not None:
            url = "notes"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_note(self, note_id, **kwargs):
        if note_id is not None and kwargs is not None:
            url = "notes/{0}".format(note_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_note(self, note_id):
        if note_id is not None:
            url = "notes/{0}".format(note_id)
            return self._delete(url)

    # Organizations section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Organizations
    def get_organizations(self, org_id=None, **kwargs):
        if org_id is not None:
            url = "organizations/{0}".format(org_id)
        else:
            url = "organizations"
        return self._get(url, **kwargs)

    def create_organization(self, **kwargs):
        if kwargs is not None:
            url = "organizations"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_organization(self, data_id, **kwargs):
        if data_id is not None:
            url = "organizations/{0}".format(data_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_organization(self, data_id):
        if data_id is not None:
            url = "organizations/{0}".format(data_id)
            return self._delete(url)

    # Persons section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Persons
    def get_persons(self, person_id=None, **kwargs):
        if person_id is not None:
            url = "persons/{0}".format(person_id)
        else:
            url = "persons"
        return self._get(url, **kwargs)

    def get_persons_by_name(self, params=None):
        if params is not None:
            url = "persons/find"
            return self._get(url, params=params)

    def create_person(self, **kwargs):
        if kwargs is not None:
            url = "persons"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_person(self, data_id, **kwargs):
        if data_id is not None and kwargs is not None:
            url = "persons/{0}".format(data_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_person(self, data_id):
        if data_id is not None:
            url = "persons/{0}".format(data_id)
            return self._delete(url)

    def get_person_deals(self, person_id, **kwargs):
        if person_id is not None:
            url = "persons/{0}/deals".format(person_id)
            return self._get(url, **kwargs)

    # Products section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Products
    def get_products(self, product_id=None, **kwargs):
        if product_id is not None:
            url = "products/{0}".format(product_id)
        else:
            url = "products"
        return self._get(url, **kwargs)

    def get_product_by_name(self, params=None):
        if params is not None:
            url = "products/find"
            return self._get(url, params=params)

    def create_product(self, **kwargs):
        if kwargs is not None:
            url = "products"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_product(self, product_id, **kwargs):
        if product_id is not None and kwargs is not None:
            url = "products/{0}".format(product_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_product(self, product_id):
        if product_id is not None:
            url = "products/{0}".format(product_id)
            return self._delete(url)

    def get_product_deal(self, product_id, **kwargs):
        if product_id is not None:
            url = "products/{0}/deals".format(product_id)
            return self._get(url, **kwargs)

    # Activities section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Activities
    def get_activities(self, activity_id=None, **kwargs):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
        else:
            url = "activities"
        return self._get(url, **kwargs)

    def create_activity(self, **kwargs):
        if kwargs is not None:
            url = "activities"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_activity(self, activity_id, **kwargs):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_activity(self, activity_id):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
            return self._delete(url)

    # Webhook section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Webhooks
    def get_hooks_subscription(self):
        url = "webhooks"
        return self._get(url)

    def create_hook_subscription(self, subscription_url, event_action, event_object, **kwargs):
        if subscription_url is not None and event_action is not None and event_object is not None:
            args = {"subscription_url": subscription_url, "event_action": event_action, "event_object": event_object}
            if kwargs is not None:
                args.update(kwargs)
            return self._post(endpoint='webhooks', json=args)
        else:
            raise Exception("The attributes necessary to create the webhook were not obtained.")

    def delete_hook_subscription(self, hook_id):
        if hook_id is not None:
            url = "webhooks/{0}".format(hook_id)
            return self._delete(url)
        else:
            raise Exception("The attributes necessary to delete the webhook were not obtained.")
