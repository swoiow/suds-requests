from collections import defaultdict
import requests
from suds.transport import Transport

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO

    StringIO = BytesIO  # PATCH: Case py3


class Requests2Transport(Transport):
    def __init__(self, **kwargs):
        Transport.__init__(self)
        self.http = requests.session()
        self.default_kw = kwargs

    def open(self, request):
        response = self.http.get(request.url, params=request.message, **self.default_kw)
        return StringIO(response.content)

    def send(self, request):
        kwargs = defaultdict(dict, **self.default_kw)
        kwargs["headers"].update(request.headers)

        response = self.http.post(request.url, data=request.message, **kwargs)
        response.headers = response.headers
        response.message = response.content
        return response
