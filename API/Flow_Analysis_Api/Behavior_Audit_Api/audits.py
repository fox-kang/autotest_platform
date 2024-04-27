import inspect
from API.Api_action import *


class audits:  # 行为审计

    def __init__(self):
        self.method = Api_method()

    def virusWarning_device(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("获取页面数据")
    def audits_taa_pagesss(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("通信协议列表")
    def filter_match_protocols(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("导出数据")
    def audits_download(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()["values"]["currentTime"]

    @allure.step('查看关键行为页面')
    def alerts_(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
