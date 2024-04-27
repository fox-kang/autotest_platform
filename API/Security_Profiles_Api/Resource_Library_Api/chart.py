import inspect
from API.Api_action import *


class chart:

    def __init__(self):
        self.method = Api_method()

    @allure.step("图标树列表")
    def group_list(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/chart-' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("图表列表")
    def chart_list(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def chart_echo(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def dynamic_query_fields(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/field/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def chart_total(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-count'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def chart_option(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-data-other'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建图标")
    def chart_save(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-other'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()["result"]

    @allure.step("复制图表")
    def chart_copy_(self, id, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + id
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑图标")
    def chart_update(self, data, cookie):  # 7
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + '-other'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()["result"]

    @allure.step("删除图标")
    def chart_delete(self, data, cookie):  # 8
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

