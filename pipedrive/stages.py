class Stages(object):
    def __init__(self, client):
        self._client = client

    def get_stage(self, stage_id, **kwargs):
        url = "stages/{}".format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_stages(self, params=None, **kwargs):
        url = "stages"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_stage_deals(self, stage_id, **kwargs):
        url = "stages/{}/deals".format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_stage(self, data, **kwargs):
        url = "stages"
        return self._client._post(self._client.BASE_URL + url, data, **kwargs)

    def update_stage(self, stage_id, data, **kwargs):
        url = "stages/{}".format(stage_id)
        return self._client._put(self._client.BASE_URL + url, data, **kwargs)

    def delete_stage(self, stage_id, **kwargs):
        url = "stages/{}".format(stage_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)
