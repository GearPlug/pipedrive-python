# pipedrive-python

pipedrive-python is an API wrapper for [Pipedrive](https://www.pipedrive.com/) written in Python.

## Installing
```
pip install pipedrive-python-lib
```

## Usage

### Using this library with OAuth 2.0

#### Client instantiation
```
from pipedrive.client import Client

client = Client('CLIENT_ID', 'CLIENT_SECRET')
```

#### Get authorization url
```
url = client.authorization_url('REDIRECT_URL')
```

#### Exchange the code for an access token
```
token = client.exchange_code('REDIRECT_URL', 'CODE')
```

#### Set access token in the library
```
client.set_access_token('ACCESS_TOKEN')
```

#### Refresh token
```
token = client.refresh_token('REFRESH_TOKEN')
```

### Using this library with API Token

#### Client instantiation
```
from pipedrive.client import Client

client = Client(domain='https://companydomain.pipedrive.com/')
```

#### Set API token in the library
```
client.set_api_token('API_TOKEN')
```

### Activities 

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Activities

#### Get an activity
```
response = client.activities.get_activity('ACTIVITY_ID')
```

#### Get all activities
```
response = client.activities.get_all_activities()
```

#### Create an activity
```
data = {
    'subject': '',
    'type': ''
}
response = client.activities.create_activity(data)
```

#### Update an activity
```
data = {
    'subject': '',
    'type': ''
}
response = client.activities.update_activity('ACTIVITY_ID', data)
```

#### Delete an activity
```
response = client.activities.delete_activity('ACTIVITY_ID')
```

#### Get activity fields
```
response = client.activities.get_activity_fields()
```

### Deals

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Deals

#### Get a deal
```
response = client.deals.get_deal('DEAL_ID')
```

#### Get all deals
```
response = client.deals.get_all_deals()
```

#### Get all deals based on filter
```
response = client.deals.get_all_deals_with_filter('FILTER_ID')
```

#### Create deal
```
data = {
    'title': ''
}
response = client.deals.create_deal(data)
```

#### Update deal
```
data = {
    'title': ''
}
response = client.deals.update_deal('DEAL_ID', data)
```

#### Delete deal
```
response = client.deals.delete_deal('DEAL_ID')
```

#### Duplicate deal
```
response = client.deals.duplicate_deal('DEAL_ID')
```

#### Get details of a deal
```
response = client.deals.get_deal_details('DEAL_ID')
```

#### Search deals
```
params = {
    'term': ''
}
response = client.deals.search_deals(params=params)
```

#### Get followers of a deal
```
response = client.deals.get_deal_followers('DEAL_ID')
```

#### Add a follower to a deal
```
response = client.deals.add_follower_to_deal('DEAL_ID', 'USER_ID')
```

#### Delete a follower from a deal
```
response = client.deals.delete_follower_to_deal('DEAL_ID', 'FOLLOWER_ID')
```

#### Get participants of a deal
```
response = client.deals.get_deal_participants('DEAL_ID')
```

#### Add a participant to a deal
```
response = client.deals.add_participants_to_deal('DEAL_ID', 'PERSON_ID')
```

#### Delete a participant from a deal
```
response = client.deals.delete_participant_to_deal('DEAL_ID', 'PARTICIPANT_ID')
```

#### Get activities associated with a deal
```
response = client.deals.get_deal_activities('DEAL_ID')
```

#### Get mail messages associated with a deal
```
response = client.deals.get_deal_mail_messages('DEAL_ID')
```

#### Get products attached to a deal
```
response = client.deals.get_deal_products('DEAL_ID')
```

#### Get deal fields
```
response = client.deals.get_deal_fields()
```

#### Get updates of a deal
```
response = client.deals.get_deal_updates('DEAL_ID')
```

### Filters

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Filters

#### Get a filter
```
response = client.filters.get_filter('FILTER_ID')
```

#### Get all filters
```
response = client.filters.get_all_filters()
```

#### Create filter
```
data = {
    'name': '', 
    'conditions': {},
    'type': ''
}
response = client.filters.create_filter(data)
```

#### Update filter
```
data = {
    'name': '', 
    'conditions': {},
    'type': ''
}
response = client.filters.update_filter('FILTER_ID', data)
```

#### Delete filter
```
response = client.filters.delete_filter('FILTER_ID')
```

### Notes

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Notes

#### Get a note
```
response = client.notes.get_note('NOTE_ID')
```

#### Get all notes
```
response = client.notes.get_all_notes()
```

#### Add a note
```
data = {
    'content': ''
}
response = client.notes.create_note(data)
```

#### Update a note
```
data = {
    'content': ''
}
response = client.notes.update_note('NOTE_ID', data)
```

#### Delete a note
```
response = client.notes.delete_note('NOTE_ID')
```

#### Get note fields
```
response = client.notes.get_note_fields()
```

### Organizations

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Organizations

#### Get an organization
```
response = client.organizations.get_organization('ORGANIZATION_ID')
```

#### Get all organizations
```
response = client.organizations.get_all_organizations()
```

#### Search organizations
```
params = {
    'term': ''
}
response = client.products.search_organizations(params=params)
```

#### Add organization
```
data = {
    'name': ''
}
response = client.organizations.create_organization(data)
```

#### Update organization
```
data = {
    'name': ''
}
response = client.organizations.update_organization('ORGANIZATION_ID', data)
```

#### Delete an organization
```
response = client.organizations.delete_organization('ORGANIZATION_ID')
```

#### Get organization fields
```
response = client.organizations.get_organization_fields()
```

### Persons 

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Persons

#### Get a person
```
response = client.persons.get_person('PERSON_ID')
```

#### Get all persons
```
response = client.persons.get_all_persons()
```

#### Search persons
```
params = {
    'term': ''
}
response = client.persons.search_persons(params=params)
```

#### Create person
```
data = {
    'name': ''
}
response = client.persons.create_person(data)
```

#### Update person
```
data = {
    'name': ''
}
response = client.persons.update_person('PERSON_ID', data)
```

#### Delete person
```
response = client.persons.delete_person('PERSON_ID')
```

#### Get deals associated with a person
```
response = client.persons.get_person_deals('PERSON_ID')
```

#### Get person fields
```
response = client.persons.get_person_fields()
```

### Pipelines

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Pipelines

#### Get a pipeline
```
response = client.pipelines.get_pipeline('PIPELINE_ID')
```

#### Get all pipelines
```
response = client.pipelines.get_all_pipelines()
```

#### Get deals attached to a pipeline
```
response = client.pipelines.get_pipeline_deals()
```

### Products

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Products

#### Get a product
```
response = client.products.get_product('PRODUCT_ID')
```

#### Get all products
```
response = client.products.get_all_products()
```

#### Search products
```
params = {
    'term': ''
}
response = client.products.search_products(params=params)
```

#### Create a product
```
data = {
    'name': ''
}
response = client.products.create_product(data)
```

#### Update a product
```
data = {
    'name': ''
}
response = client.products.update_product('PRODUCT_ID', data)
```

#### Delete a product
```
response = client.products.delete_product('PRODUCT_ID')
```

#### Get deals where a product is attached to
```
response = client.products.get_product_deal('PRODUCT_ID')
```

#### Get product fields
```
response = client.products.get_product_fields()
```

### Recents

#### Get recent changes
```
params = {
    'since_timestamp': 'YYYY-MM-DD HH:MM:SS'
}
response = client.recents.get_recent_changes(params=params)
```

### Users 

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Users

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

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Webhooks

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
