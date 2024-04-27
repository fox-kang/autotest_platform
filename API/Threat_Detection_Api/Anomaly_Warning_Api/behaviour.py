import inspect
from API.Api_action import *


class behaviour:

    def __init__(self):
        self.method = Api_method()

    @allure.step("异常行为列表")
    def alerts_(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("打开异常行为")
    def filter_match_protocols(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def alerts_dispose_(self, alarmID, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + alarmID
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("提交处置异常行为")
    def alerts_dispose_addOrUpdate(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("取证")
    def alert_download_pcap(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("添加白名单")
    def protocols_all(self, filterFlag, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + filterFlag
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp
