class Organizations(object):
    def __init__(self, client):
        self._client = client

    def get_organization(self, organization_id, **kwargs):
        url = "organizations/{}".format(organization_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_organizations(self, params=None, **kwargs):
        url = "organizations"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_organization(self, data, **kwargs):
        url = "organizations"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_organization(self, organization_id, data, **kwargs):
        url = "organizations/{}".format(organization_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_organization(self, organization_id, **kwargs):
        url = "organizations/{}".format(organization_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_organization_fields(self, params=None, **kwargs):
        url = "organizationFields"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def search_organizations(self, params=None, **kwargs):
        url = "organizations/search"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_organization_persons(self, organization_id, params=None, **kwargs):
        url = "organizations/{}/persons".format(organization_id)
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)
