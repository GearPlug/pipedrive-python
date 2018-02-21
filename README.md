# pipedrive-python
Pipedrive API wrapper for Pypedrive written in Python.

## Installing
```
git+git://github.com/GearPlug/pipedrive-python
```

## Usage
```
from pipedrive.client import Client
client = Client('CLIENT_ID', 'CLIENT_SECRET', 'OPTIONAL - access_token')
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

#### Set token
```
token = client.set_token('TOKEN')
```

## Requirements
- requests
- base64 -- b64encode
- urllib.parse -- urlencode

## Tests
```
pipedrive/test.py
```
