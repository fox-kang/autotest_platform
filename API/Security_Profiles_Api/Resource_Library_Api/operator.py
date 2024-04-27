import inspect
from API.Api_action import *


class operator:

    def __init__(self):
        self.method = Api_method()

    def types_operators(self, types, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '?')
        url = Public().handle_str() + '/tsa/api/' + url_route + types
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("协议库列表")
    def protocols(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建协议")
    def protocols_add(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑协议")
    def protocols_update(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除协议")
    def protocols_delete_ids(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
