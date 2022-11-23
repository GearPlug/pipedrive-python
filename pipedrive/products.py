class Products(object):
    def __init__(self, client):
        self._client = client

    def get_product(self, product_id, **kwargs):
        url = "products/{}".format(product_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_products(self, **kwargs):
        url = "products"
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def search_products(self, params=None, **kwargs):
        url = "products/search"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_product(self, data, **kwargs):
        url = "products"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_product(self, product_id, data, **kwargs):
        url = "products/{}".format(product_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_product(self, product_id, **kwargs):
        url = "products/{}".format(product_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_product_deal(self, product_id, **kwargs):
        url = "products/{}/deals".format(product_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_product_fields(self, **kwargs):
        url = "productFields"
        return self._client._get(self._client.BASE_URL + url, **kwargs)
