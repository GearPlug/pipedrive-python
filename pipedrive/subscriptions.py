class Subscriptions(object):
    def __init__(self, client):
        self._client = client

    def get_subscription(self, subscription_id, **kwargs):
        url = "subscriptions/{}".format(subscription_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deal_subscription(self, deal_id, **kwargs):
        url = "subscriptions/find/{}".format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_payments(self, subscription_id, **kwargs):
        url = "subscriptions/{}/payments".format(subscription_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_recurring_subscription(self, data, **kwargs):
        url = "subscriptions/recurring"
        return self._client._post(self._client.BASE_URL + url, data, **kwargs)

    def add_installment_subscription(self, data, **kwargs):
        url = "subscriptions/installment"
        return self._client._post(self._client.BASE_URL + url, data, **kwargs)

    def update_recurring_subscription(self, subscription_id, data, **kwargs):
        url = "subscriptions/recurring/{}".format(subscription_id)
        return self._client._put(self._client.base_url + url, data, **kwargs)

    def update_installment_subscription(self, subscription_id, data, **kwargs):
        url = "subscriptions/installment/{}".format(subscription_id)
        return self._client._put(self._client.base_url + url, data, **kwargs)

    def cancel_recurring_subscription(self, subscription_id, data, **kwargs):
        url = "subscriptions/recurring/{}/cancel".format(subscription_id)
        return self._client._put(self._client.base_url + url, data, **kwargs)

    def delete_subscription(self, subscription_id, **kwargs):
        url = "subscriptions/{}".format(subscription_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)
