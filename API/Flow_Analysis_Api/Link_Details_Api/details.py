import inspect
from API.Api_action import *


class details:

    def __init__(self):
        self.method = Api_method()

    def topology_getTopoDetailPage(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def topology_getProtocolsByFilter(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

