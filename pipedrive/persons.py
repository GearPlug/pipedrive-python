class Persons(object):
    def __init__(self, client):
        self._client = client

    def get_person(self, person_id, **kwargs):
        url = "persons/{}".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_persons(self, params=None, **kwargs):
        url = "persons"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def search_persons(self, params=None, **kwargs):
        url = "persons/search"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_person(self, data, **kwargs):
        url = "persons"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_person(self, person_id, data, **kwargs):
        url = "persons/{}".format(person_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_person(self, person_id, **kwargs):
        url = "persons/{}".format(person_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_person_deals(self, person_id, **kwargs):
        url = "persons/{}/deals".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_person_fields(self, params=None, **kwargs):
        url = "personFields"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_person_activities(self, person_id, **kwargs):
        url = "persons/{}/activities".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
