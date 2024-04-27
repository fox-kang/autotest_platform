import inspect
from API.Api_action import *


class backup:

    def __init__(self):
        self.method = Api_method()

    @allure.step("新建基础数据外发")
    def transmit_template_getAll(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑基础数据外发")
    def add_or_update(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/transmit/task/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取基础数据外发列表")
    def transmit_task_list(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑基础数据外发使能状态")
    def update_active_flag(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/api/transmit/task/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除基础数据外发")
    def transmit_task_delete(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取专项数据外发列表")
    def specialConfig_getAllSpecialConfig(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取专项数据外发外发方式")
    def specialConfig_getAllSendMethod(self, platformId, templateId, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + platformId + '&' + templateId
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("专项数据外发配置参数")
    def specialConfig_getAllDefaultConfig(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建专项数据外发")
    def specialConfig_getAllTemplate(self, platformId, templateId, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + platformId + '&' + templateId
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("确定新建专项数据外发")
    def specialConfig_manager_add(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

