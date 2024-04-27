import inspect
from API.Api_action import *


class risk:

    def __init__(self):
        self.method = Api_method()

    def high_risk_port(self, data, path, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '-')
        url = Public().handle_str() + '/tsa/' + url_route + '/' + path
        if path == 'configuration':
            rsp = self.method.http_get(url, None, None, cookie)
            return rsp
        else:
            rsp = self.method.http_post_json(url, data, None, None, cookie)
            return rsp

