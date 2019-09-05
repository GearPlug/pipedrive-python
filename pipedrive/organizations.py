class Organizations(object):
    def __init__(self, client):
        self._client = client

    def get_organizations(self, org_id=None, **kwargs):
        if org_id is not None:
            url = 'organizations/{}'.format(org_id)
        else:
            url = 'organizations'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_organization(self, data, **kwargs):
        url = 'organizations'
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_organization(self, organization_id, data, **kwargs):
        url = 'organizations/{}'.format(organization_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_organization(self, organization_id, **kwargs):
        url = 'organizations/{}'.format(organization_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)
