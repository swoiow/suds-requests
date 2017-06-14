# suds-requests
A suds transport implemented with requests.

# Examples
```
from functools import partial

from suds.client import Client

from Transport import Requests2Transport

proxy = dict(http='http://127.0.0.1:12345')
http = Requests2Transport(headers=headers, proxies=proxy)
Client = partial(Client, transport=http)

client = Client(url)
```
