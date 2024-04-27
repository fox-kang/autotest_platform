import inspect

import allure

from API.Api_action import *


class kbi: # 关键行为

    def __init__(self):
        self.method = Api_method()

    @allure.step('关键行为列表')
    def alerts_(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def filter_match_protocols(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/audits/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('获取页面时间戳')
    def time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()['values']['currentTime']

    @allure.step('关键行为取证')
    def alerts_download_pcap(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
