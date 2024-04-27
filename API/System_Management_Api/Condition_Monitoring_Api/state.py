import inspect
from API.Api_action import *


class state:

    def __init__(self):
        self.method = Api_method()

    @allure.step("CPU")
    def zabbix_item_server_cpu(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("阈值设置")
    def server_trigger_get(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/dashboards/system_alarm/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def zabbix_item_JITData_server(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改阈值")
    def server_trigger_update(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/dashboards/system_alarm/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
