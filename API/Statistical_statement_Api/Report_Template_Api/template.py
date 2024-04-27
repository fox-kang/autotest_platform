import inspect
from API.Api_action import *


class template:

    def __init__(self):
        self.method = Api_method()

    @allure.step("所属报表模版")
    def group_list(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-template-' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("报表文件列表")
    def accessory_list(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '-')
        url = Public().handle_str() + '/tsa/report-template/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("报表文件策略列表")
    def accessory_statistics(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '-')
        url = Public().handle_str() + '/tsa/report-template/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("下载报表文件")
    def accessory_down(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '-')
        url = Public().handle_str() + '/tsa/report-template/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除报表")
    def accessory_delete(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '-')
        url = Public().handle_str() + '/tsa/report-template/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp



