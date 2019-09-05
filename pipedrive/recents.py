class Recents(object):
    def __init__(self, client):
        self._client = client

    def get_recent_changes(self, **kwargs):
        url = 'recents'
        return self._client._get(self._client.BASE_URL + url, **kwargs)
