import inspect

import allure

from API.Api_action import *


class resource:  # 工控关键行为库

    def __init__(self):
        self.method = Api_method()

    def enums_(self, severity, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + severity
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def enums(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('资源库页面')
    def templates_page(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("关键行为库页面")
    def rules_page(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("查看详情")
    def vulnerability_intrusion_rules(self, id, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + id
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改使能状态")
    def rules_editSeverityEnable(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

