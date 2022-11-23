class Activities(object):
    def __init__(self, client):
        self._client = client

    def get_activity(self, activity_id, **kwargs):
        url = "activities/{}".format(activity_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_activities(self, params=None, **kwargs):
        url = "activities"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_activity(self, data, **kwargs):
        url = "activities"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_activity(self, activity_id, data, **kwargs):
        url = "activities/{}".format(activity_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_activity(self, activity_id, **kwargs):
        url = "activities/{}".format(activity_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_activity_fields(self, params=None, **kwargs):
        url = "activityFields"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)
