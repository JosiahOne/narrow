# Example program based on requests 2.19 which is vulnerable to info disclosure
# when calling get with basic auth credentials
#
# rebuild_auth is one function related to the fix:
#   https://github.com/psf/requests/commit/c45d7c49ea75133e52ab22a8e9e13173938e36ff

import requests
requests.get('https://localhost:4443', auth=('hello', 'world'), verify=False)
