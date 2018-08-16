# pipedrive-python
Pipedrive API wrapper for Pypedrive written in Python.

## Installing
```
pip install pipedrive-python-lib
```

## Usage
- If you are not going to use the authentication flow, just send the "pipedrive company domain" and instance the library like this:
```
from pipedrive.client import Client
client = Client(api_base_url='https://companydomain.pipedrive.com/')
```

- If on the contrary you will use it, send the "pipedrive company domain", the "client_id", the "client secret" and the parameter "oauth=True" in the main instance like this:
```
from pipedrive.client import Client
client = Client(api_base_url='https://companydomain.pipedrive.com/', 'CLIENT_ID', 'CLIENT_SECRET', oauth=True)
```

#### Set token
And to make requests send the access token
```
client.set_token(access_token)
```

#### Get authorization url
```
url = client.get_oauth_uri("REDIRECT_URL", "OPTIONAL - state")
```

#### Exchange the code for an access token
```
token = client.exchange_code('REDIRECT_URL', 'CODE')
```

#### Refresh token
```
token = client.refresh_token('REFRESH TOKEN')
```

#### Get recent changes
```
token = client.get_recent_changes(since_timestamp="YYYY-MM-DD HH:MM:SS")
```

### Deals section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Deals

#### Get deals
If you need a specific deal send the deal id, if you don't just call the method
```
get_specific_deal = client.get_deals(deal_id="")

get_deals = client.get_deals()
```

#### Create deal
```
create_deal = client.create_deal(title="")
```

#### Update deal
```
update_deal = client.update_deal(deal_id="")
```

#### Delete deal
```
delete_deal = client.delete_deal(deal_id="")
```

#### Duplicate deal
```
duplicate_deal = client.duplicate_deal(deal_id="")
```

#### Get details of a deal
```
details_deal = client.get_deal_details(deal_id="")
```

#### Find deals by name
```
find_deal = client.get_deals_by_name(term="")
```

#### Get followers of a deal
```
followers_deal = client.get_deal_followers(deal_id="")
```

#### Add a follower to a deal
```
add_follower_deal = client.add_follower_to_deal(deal_id="", user_id="")
```

#### Delete a follower from a deal
```
delete_followers_deal = client.delete_follower_to_deal(deal_id="", follower_id="")
```

#### Get participants of a deal
```
get_participants_deal = client.get_deal_participants(deal_id="")
```

#### Add a participant to a deal
```
add_participants_deal = client.add_participants_to_deal(deal_id="", person_id="")
```

#### Delete a participant from a deal
```
delete_participants_deal = client.delete_participant_to_deal(deal_id="", participant_id="")
```

#### Get activities associated with a deal
```
get_activities_deal = client.get_deal_activities(deal_id="")
```

#### Get mail messages associated with a deal
```
get_messages_deal = client.get_deal_mail_messages(deal_id="")
```

#### Get products attached to a deal
```
get_products_deal = client.get_deal_products(deal_id="")
```

### Notes section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Notes

#### Get notes
If you need a specific note send the note id, if you don't just call the method
```
get_specific_note = client.get_notes(note_id="")

get_notes = client.get_notes()
```

#### Add a note
```
add_note = client.create_note(content="", org_id="")
```

#### Update a note
```
update_note = client.update_note(note_id="", content="")
```

#### Delete a note
```
delete_note = client.delete_note(note_id="")
```

### Organizations section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Organizations

#### Get organizations
If you need a specific organization send the organization id, if you don't just call the method
```
get_specific_organization = client.get_organizations(org_id="")

get_organizations = client.get_organizations()
```

#### Add organization
```
add_organization = client.create_organization(name="")
```

#### Update organization
```
update_organization = client.update_organization(data_id="", name="")
```

#### Delete an organization
```
delete_organization = client.delete_organization(data_id="")
```

### Persons section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Persons

#### Get persons
If you need the details of a person send the person id, if you don't just call the method
```
get_details_person = client.get_persons(person_id="")

get_persons = client.get_persons()
```

#### Get persons by name
```
find_persons = client.get_persons_by_name(term="")
```

#### Create person
```
add_persons = client.create_person(name="")
```

#### Update person
```
update_persons = client.update_person(data_id="", name="")
```

#### Delete person
```
delete_persons = client.delete_person(data_id="")
```

#### Get deals associated with a person
```
get_persons_deals = client.get_person_deals(person_id="")
```


### Products section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Products

#### Get products
If you need a specific product send the product id, if you don't just call the method
```
get_specific_product = client.get_products(product_id="")

get_products = client.get_products()
```

#### Get products by name
```
find_product = client.get_product_by_name(term="")
```

#### Create a product
```
add_product = client.create_product(name="")
```

#### Update a product
```
update_product = client.update_product(product_id="", name="")
```

#### Delete a product
```
delete_product = client.delete_product(product_id="")
```

#### Get deals where a product is attached to
```
get_product_deal = client.get_product_deal(product_id="")
```

### Activities section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Activities

#### Get activities
If you need the activity details send the activity id, if you don't just call the method
```
get_details_activity = client.get_activities(activity_id="")

get_activities = client.get_activities()
```

#### Create an activity
```
add_activity = client.create_activity(subject="", type="")
```

#### Update an activity
```
edit_activity = client.update_activity(activity_id="")
```

#### Delete an activity
```
delete_activity = client.delete_activity(activity_id="")
```

### Webhook section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Webhooks

#### Get webhooks
```
get_hooks = client.get_hooks_subscription()
```

#### Add webhook
```
add_hook = client.create_hook_subscription(subscription_url="", event_action="", event_object="")
```

#### Delete webhook
```
delete_hooks = client.delete_hook_subscription(hook_id="")
```

### Users section, see the api documentation: https://developers.pipedrive.com/docs/api/v1/#!/Users

#### Get users
```
users = client.get_users(user_id="")
```

## Requirements
- requests


## Contributing
```
Fork it ( https://github.com/GearPlug/pipedrive-python/fork )
Create your feature branch (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create a new Pull Request
```
