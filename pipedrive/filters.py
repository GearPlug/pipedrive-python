class Filters(object):
    def __init__(self, client):
        self._client = client

    def get_filter(self, filter_id, **kwargs):
        url = "filters/{}".format(filter_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_filters(self, params=None, **kwargs):
        url = "filters"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_filter(self, data, **kwargs):
        url = "filters"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_filter(self, filter_id, data, **kwargs):
        url = "filters/{}".format(filter_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_filter(self, filter_id, **kwargs):
        url = "filters/{}".format(filter_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)
