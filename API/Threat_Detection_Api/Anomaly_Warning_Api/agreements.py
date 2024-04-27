import inspect
from API.Api_action import *


class agreements:

    def __init__(self):
        self.method = Api_method()

    @allure.step("获取可疑协议列表")
    def alerts_asset(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + '-alarm'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("可疑协议详情")
    def alerts_alarm(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + '-link-detail'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("可以协议处置")
    def alerts_dispose_(self, alarmID, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + alarmID
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("添加白名单")
    def alerts_dispose_addOrUpdate(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

