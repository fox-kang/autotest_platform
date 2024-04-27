import inspect

import allure

from API.Api_action import *


class statistics:

    def __init__(self):
        self.method = Api_method()

    @allure.step('查看ip流量分布')
    def statsdata_getIpFlowTopTen(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('查看会话历史流量记录')
    def statsdata_getHistoricalFlowRecordByCondition(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('查看链路流量分析')
    def statsdata_getRangeFromFlowStatByCondition(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('查看历史总流量分析')
    def total_traffic_history(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/statsdata/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step('查看实时流量分析')
    def statsdata_getNetCardTraffic(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def statsdata_getAllProtocolNames(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    

