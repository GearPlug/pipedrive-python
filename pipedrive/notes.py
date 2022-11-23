class Notes(object):
    def __init__(self, client):
        self._client = client

    def get_note(self, note_id, **kwargs):
        url = "notes/{}".format(note_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_notes(self, params=None, **kwargs):
        url = "notes"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_note(self, data, **kwargs):
        url = "notes"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_note(self, note_id, data, **kwargs):
        url = "notes/{}".format(note_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_note(self, note_id, **kwargs):
        url = "notes/{}".format(note_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_note_fields(self, params=None, **kwargs):
        url = "noteFields"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)
