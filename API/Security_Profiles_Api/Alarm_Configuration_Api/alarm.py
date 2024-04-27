import inspect
from API.Api_action import *


class alarm:  # 告警通知配置

    def __init__(self):
        self.method = Api_method()

    def enums_(self, severity, type, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '?')
        url = Public().handle_str() + '/tsa/api/' + url_route + severity + type
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def enums(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("告警通知配置列表")
    def alarm_notice_list(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def alarm_notice_initialData(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def users_contactList(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("新建告警通知配置")
    def alarm_notice_add(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def alarm_notice_detail(self, id, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '?')
        url = Public().handle_str() + '/tsa/api/' + url_route + id
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑策略")
    def alarm_notice_update(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '?')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除策略")
    def alarm_notice_delete(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("使能/禁用策略")
    def alarm_notice_enables(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

