class Pipelines(object):
    def __init__(self, client):
        self._client = client

    def get_pipeline(self, pipeline_id, **kwargs):
        url = "pipelines/{}".format(pipeline_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_pipelines(self, **kwargs):
        url = "pipelines"
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_pipeline_deals(self, pipeline_id, **kwargs):
        url = "pipelines/{}/deals".format(pipeline_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
