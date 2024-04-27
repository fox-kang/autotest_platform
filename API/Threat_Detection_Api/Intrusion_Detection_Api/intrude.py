import inspect

import allure

from API.Api_action import *
from common.threat_public import *


class intrude:  # 入侵检测

    def __init__(self):
        self.method = Api_method()

    @allure.step("获取时间戳")
    def time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()["values"]["currentTime"]

    @allure.step("入侵检测数据列表")
    def alerts_(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("打开入侵检测")
    def filter_match_protocols(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("入侵检测类型")
    def alerts_getPolicyRuleType_1(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("查看详情")
    def intrusion_rules_ex(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = (Public().handle_str() + '/tsa/api/vulnerability/' + url_route + '?'
               + intrude().alerts_(data, cookie).json()["values"]["result"]["generic"]["rule_id"])
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("处置")
    def alerts_dispose_addOrUpdate(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("添加例外")
    def policies_exclude_add(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
