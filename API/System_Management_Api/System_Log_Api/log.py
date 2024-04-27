import inspect

import allure

from API.Api_action import *


class log:

    def __init__(self):
        self.method = Api_method()

    @allure.step("获取日志类型列表")
    def enums(self, operate, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + operate
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("获取日志日志列表")
    def pg_logs_operationLogList(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取页面时间戳")
    def time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()['values']['currentTime']
