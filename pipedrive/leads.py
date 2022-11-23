class Leads(object):
    def __init__(self, client):
        self._client = client

    def get_lead(self, lead_id, **kwargs):
        url = "leads/{}".format(lead_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_leads(self, **kwargs):
        url = "leads"
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_lead(self, data, **kwargs):
        url = "leads"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_lead(self, lead_id, data, **kwargs):
        url = "leads/{}".format(lead_id)
        return self._client._patch(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_lead(self, lead_id, **kwargs):
        url = "leads/{}".format(lead_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_lead_details(self, lead_id, **kwargs):
        url = "leads/{}".format(lead_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
