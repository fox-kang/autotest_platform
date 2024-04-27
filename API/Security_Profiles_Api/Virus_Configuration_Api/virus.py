import inspect
from API.Api_action import *


class antivirus:

    def __init__(self):
        self.method = Api_method()

    def antivirus_filetype_get(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("病毒配置列表")
    def antivirus_template_get(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建病毒配置")
    def antivirus_template_add(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑病毒配置")
    def antivirus_template_update(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除病毒配置")
    def antivirus_template_delete(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
