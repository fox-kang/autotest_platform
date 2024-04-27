import inspect
from API.Api_action import *


class record:

    def __init__(self):
        self.method = Api_method()

    @allure.step("报表列表")
    def template_list(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新增模版目录")
    def group_create(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-template-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑模版目录")
    def group_update(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-template-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除模版目录")
    def group_delete(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-template-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建报表")
    def template_create(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑报表")
    def template_fetch(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("修改报表")
    def template_update(self, data, cookie):  # 7
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("下载报表")
    def template_down(self, data, cookie):  # 8
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def plan_fetch_(self, templateId, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route + templateId
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    def plan_save(self, data, cookie):  # 9
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("报表模板复制")
    def template_copy_(self, templateId, cookie):  # 10
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route + templateId
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("删除报表模版")
    def template_delete(self, data, cookie):  # 11
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/report-' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp