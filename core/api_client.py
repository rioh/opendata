import requests

class ApiClient(object):
    # TODO
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.kwargs = kwargs
