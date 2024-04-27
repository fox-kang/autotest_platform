import inspect
from API.Api_action import *


class flows:

    def __init__(self):
        self.method = Api_method()

    @allure.step("异常流量列表")
    def alerts_(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + '-alarm'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("打开异常流量")
    def filter_match_protocols(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("调整基线配置")
    def baseline_flow_key(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("修改基线配置")
    def baseline_flow_update(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
