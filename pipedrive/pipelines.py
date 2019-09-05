class Pipelines(object):
    def __init__(self, client):
        self._client = client

    def get_pipelines(self, pipeline_id=None, **kwargs):
        if pipeline_id is not None:
            url = 'pipelines/{}'.format(pipeline_id)
        else:
            url = 'pipelines'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_pipeline_deals(self, pipeline_id, **kwargs):
        url = 'pipelines/{}/deals'.format(pipeline_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
