class Filters(object):
    def __init__(self, client):
        self._client = client

    def get_filters(self, filter_id=None, **kwargs):
        if filter_id is not None:
            url = 'filters/{}'.format(filter_id)
        else:
            url = 'filters'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_filter(self, data, **kwargs):
        url = 'filters'
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_filter(self, filter_id, data, **kwargs):
        url = 'filters/{}'.format(filter_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_filter(self, filter_id, **kwargs):
        url = 'filters/{}'.format(filter_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)
