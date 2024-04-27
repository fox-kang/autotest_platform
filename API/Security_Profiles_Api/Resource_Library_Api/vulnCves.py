import inspect
from API.Api_action import *


class vulnCves:

    def __init__(self):
        self.method = Api_method()

    def vulnCves_select(self, data, path, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + path

        if path == '-CveEnums':  # 1  危害等级
            rsp = self.method.http_get(url, None, None, cookie)
            return rsp
        elif path == '-CveCategory':  # 4
            rsp = self.method.http_get(url, None, None, cookie)
            return rsp
        elif path == '-VulnCveChart':  # 2
            rsp = self.method.http_post_json(url, data, None, None, cookie)  # 1
            return rsp
        elif path == '-CveList':  # 3
            rsp = self.method.http_post_json(url, data, None, None, cookie)  # 2
            return rsp

    def assetModel(self, data, path, cookie):  # 3 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + path
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def assetModel_getModelByVendor(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def vulnCves_add(self, data, path, cookie):  # 5 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + path
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def vulnCves_update(self, data, path, cookie):  # 6 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + path
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def vulnCves_delete(self, data, path, cookie):  # 7 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + path
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

