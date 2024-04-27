import inspect
from API.Api_action import *


class organization:

    def __init__(self):
        self.method = Api_method()

    @allure.step("组织单元列表")
    def organization_type(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("组织单元管理列表")
    def organization_list(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建组织单元")
    def organization_save(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-unit'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑组织单元")
    def organization_update(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-unit'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("移动组织单元")
    def organization_move(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-org'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除组织单元")
    def organization_delete(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-unit'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp