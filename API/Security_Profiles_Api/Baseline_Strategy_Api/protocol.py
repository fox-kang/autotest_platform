import inspect
import allure
from API.Api_action import *
from common.baseline_public import *


class protocol:
    def __init__(self):
        self.method = Api_method()

    @allure.step("新建协议基线")
    def baseline_protocol_getAllProtocols(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("选择新增的协议基线并确定")
    def baseline_protocol_add(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_or_update'
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data2'], None, None, cookie)
        return rsp

    @allure.step("删除协议基线并确定")
    def baseline_protocol_delete(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data3'], None, None, cookie)
        return rsp

    @allure.step("协议基线列表")
    def baseline_protocol_list(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data4'], None, None, cookie)
        return rsp

    @allure.step("应用协议基线")
    def baseline_protocol_configuration(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data5'], None, None, cookie)
        return rsp

    @allure.step("协议基线状态")
    def baselineConfigLog_status(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data6'], None, None, cookie)
        return rsp

    @allure.step("修改协议基线状态")
    def baseline_protocol_change(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '-status'
        rsp = self.method.http_post_json(url, a.read_yml_file(protocol_file)['data7'], None, None, cookie)
        return rsp
