class Persons(object):
    def __init__(self, client):
        self._client = client

    def get_persons(self, person_id=None, **kwargs):
        if person_id is not None:
            url = 'persons/{}'.format(person_id)
        else:
            url = 'persons'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_persons_by_name(self, **kwargs):
        url = 'persons/find'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_person(self, data, **kwargs):
        url = 'persons'
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_person(self, person_id, data, **kwargs):
        url = 'persons/{}'.format(person_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_person(self, person_id, **kwargs):
        url = 'persons/{}'.format(person_id)
        return self._client._delete(url, **kwargs)

    def get_person_deals(self, person_id, **kwargs):
        url = 'persons/{}/deals'.format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
