# pipedrive-python
![](https://img.shields.io/badge/version-1.2.3-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)
*pipedrive-python* is an API wrapper for [Pipedrive](https://www.pipedrive.com/) written in Python.

## Installing
```
pip install pipedrive-python-lib
```

## Usage

### Using this library with OAuth 2.0

#### Client instantiation
```python
from pipedrive.client import Client

client = Client('CLIENT_ID', 'CLIENT_SECRET')
```

#### Get authorization url
```python
url = client.authorization_url('REDIRECT_URL')
```

#### Exchange the code for an access token
```python
token = client.exchange_code('REDIRECT_URL', 'CODE')
```

#### Set access token in the library
```python
client.set_access_token('ACCESS_TOKEN')
```

#### Refresh token
```python
token = client.refresh_token('REFRESH_TOKEN')
```

### Using this library with API Token

#### Client instantiation
```python
from pipedrive.client import Client

client = Client(domain='https://companydomain.pipedrive.com/')
```

#### Set API token in the library
```python
client.set_api_token('API_TOKEN')
```

### Activities

API docs: https://developers.pipedrive.com/docs/api/v1/Activities

#### Get an activity
```python
response = client.activities.get_activity('ACTIVITY_ID')
```

#### Get all activities
```python
response = client.activities.get_all_activities()
```

#### Create an activity
```python
data = {
    'subject': '',
    'type': ''
}
response = client.activities.create_activity(data)
```

#### Update an activity
```python
data = {
    'subject': '',
    'type': ''
}
response = client.activities.update_activity('ACTIVITY_ID', data)
```

#### Delete an activity
```python
response = client.activities.delete_activity('ACTIVITY_ID')
```

#### Get activity fields
```python
response = client.activities.get_activity_fields()
```

### Deals

API docs: https://developers.pipedrive.com/docs/api/v1/Deals

#### Get a deal
```python
response = client.deals.get_deal('DEAL_ID')
```

#### Get all deals
```python
response = client.deals.get_all_deals()
```

#### Get all deals based on filter
```python
response = client.deals.get_all_deals_with_filter('FILTER_ID')
```

#### Create deal
```python
data = {
    'title': ''
}
response = client.deals.create_deal(data)
```

#### Update deal
```python
data = {
    'title': ''
}
response = client.deals.update_deal('DEAL_ID', data)
```

#### Delete deal
```python
response = client.deals.delete_deal('DEAL_ID')
```

#### Duplicate deal
```python
response = client.deals.duplicate_deal('DEAL_ID')
```

#### Get details of a deal
```python
response = client.deals.get_deal_details('DEAL_ID')
```

#### Search deals
```python
params = {
    'term': ''
}
response = client.deals.search_deals(params=params)
```

#### Get followers of a deal
```python
response = client.deals.get_deal_followers('DEAL_ID')
```

#### Add a follower to a deal
```python
response = client.deals.add_follower_to_deal('DEAL_ID', 'USER_ID')
```

#### Delete a follower from a deal
```python
response = client.deals.delete_follower_to_deal('DEAL_ID', 'FOLLOWER_ID')
```

#### Get participants of a deal
```python
response = client.deals.get_deal_participants('DEAL_ID')
```

#### Add a participant to a deal
```python
response = client.deals.add_participants_to_deal('DEAL_ID', 'PERSON_ID')
```

#### Delete a participant from a deal
```python
response = client.deals.delete_participant_to_deal('DEAL_ID', 'PARTICIPANT_ID')
```

#### Get activities associated with a deal
```python
response = client.deals.get_deal_activities('DEAL_ID')
```

#### Get mail messages associated with a deal
```python
response = client.deals.get_deal_mail_messages('DEAL_ID')
```

#### Get products attached to a deal
```python
response = client.deals.get_deal_products('DEAL_ID')
```

#### Get deal fields
```python
response = client.deals.get_deal_fields()
```

#### Get updates of a deal
```python
response = client.deals.get_deal_updates('DEAL_ID')
```

### Filters

API docs: https://developers.pipedrive.com/docs/api/v1/Filters

#### Get a filter
```python
response = client.filters.get_filter('FILTER_ID')
```

#### Get all filters
```python
response = client.filters.get_all_filters()
```

#### Create filter
```python
data = {
    'name': '',
    'conditions': {},
    'type': ''
}
response = client.filters.create_filter(data)
```

#### Update filter
```python
data = {
    'name': '',
    'conditions': {},
    'type': ''
}
response = client.filters.update_filter('FILTER_ID', data)
```

#### Delete filter
```python
response = client.filters.delete_filter('FILTER_ID')
```

### Notes

API docs: https://developers.pipedrive.com/docs/api/v1/Notes

#### Get a note
```python
response = client.notes.get_note('NOTE_ID')
```

#### Get all notes
```python
response = client.notes.get_all_notes()
```

#### Add a note
```python
data = {
    'content': ''
}
response = client.notes.create_note(data)
```

#### Update a note
```python
data = {
    'content': ''
}
response = client.notes.update_note('NOTE_ID', data)
```

#### Delete a note
```python
response = client.notes.delete_note('NOTE_ID')
```

#### Get note fields
```python
response = client.notes.get_note_fields()
```

### Organizations

API docs: https://developers.pipedrive.com/docs/api/v1/Organizations

#### Get an organization
```python
response = client.organizations.get_organization('ORGANIZATION_ID')
```

#### Get all organizations
```python
response = client.organizations.get_all_organizations()
```

#### Search organizations
```python
params = {
    'term': ''
}
response = client.products.search_organizations(params=params)
```

#### Add organization
```python
data = {
    'name': ''
}
response = client.organizations.create_organization(data)
```

#### Update organization
```python
data = {
    'name': ''
}
response = client.organizations.update_organization('ORGANIZATION_ID', data)
```

#### Delete an organization
```python
response = client.organizations.delete_organization('ORGANIZATION_ID')
```

#### Get organization fields
```python
response = client.organizations.get_organization_fields()
```

#### Get organization activities
```python
response = client.organizations.get_organization_activities('ORGANIZATION_ID')
```

### Persons

API docs: https://developers.pipedrive.com/docs/api/v1/Persons

#### Get a person
```python
response = client.persons.get_person('PERSON_ID')
```

#### Get all persons
```python
response = client.persons.get_all_persons()
```

#### Search persons
```python
params = {
    'term': ''
}
response = client.persons.search_persons(params=params)
```

#### Create person
```python
data = {
    'name': ''
}
response = client.persons.create_person(data)
```

#### Update person
```python
data = {
    'name': ''
}
response = client.persons.update_person('PERSON_ID', data)
```

#### Delete person
```python
response = client.persons.delete_person('PERSON_ID')
```

#### Get deals associated with a person
```python
response = client.persons.get_person_deals('PERSON_ID')
```

#### Get person fields
```python
response = client.persons.get_person_fields()
```

### Pipelines

API docs: https://developers.pipedrive.com/docs/api/v1/Pipelines

#### Get a pipeline
```python
response = client.pipelines.get_pipeline('PIPELINE_ID')
```

#### Get all pipelines
```python
response = client.pipelines.get_all_pipelines()
```

#### Get deals attached to a pipeline
```python
response = client.pipelines.get_pipeline_deals()
```

### Products

API docs: https://developers.pipedrive.com/docs/api/v1/Products

#### Get a product
```python
response = client.products.get_product('PRODUCT_ID')
```

#### Get all products
```python
response = client.products.get_all_products()
```

#### Search products
```python
params = {
    'term': ''
}
response = client.products.search_products(params=params)
```

#### Create a product
```python
data = {
    'name': ''
}
response = client.products.create_product(data)
```

#### Update a product
```python
data = {
    'name': ''
}
response = client.products.update_product('PRODUCT_ID', data)
```

#### Delete a product
```python
response = client.products.delete_product('PRODUCT_ID')
```

#### Get deals where a product is attached to
```python
response = client.products.get_product_deal('PRODUCT_ID')
```

#### Get product fields
```python
response = client.products.get_product_fields()
```

### Recents

#### Get recent changes
```python
params = {
    'since_timestamp': 'YYYY-MM-DD HH:MM:SS'
}
response = client.recents.get_recent_changes(params=params)
```
### Leads
API docs: https://developers.pipedrive.com/docs/api/v1/Leads

#### Get a lead
```python
response = client.leads.get_lead('LEAD_ID')
```
#### Search leads
```python
params = {
    'term': ''
}
response = client.leads.search_leads(params=params)
```
### Users

API docs: https://developers.pipedrive.com/docs/api/v1/Users

#### Get an user
```
response = client.users.get_user('USER_ID')
```

#### Get all users
```
response = client.users.get_all_users()
```

#### Get me
```
response = client.users.get_me()
```

### Webhook

API docs: https://developers.pipedrive.com/docs/api/v1/Webhooks

#### Get webhooks
```
response = client.webhooks.get_hooks_subscription()
```

#### Add webhook
```
data = {
    'subscription_url': '',
    'event_action': '',
    'event_object': ''
}
response = client.webhooks.create_hook_subscription(data)
```

#### Delete webhook
```
response = client.webhooks.delete_hook_subscription('HOOK_ID')
```

## Requirements
- requests


## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.

#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/pipedrive-python/issues).

#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/pipedrive-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
