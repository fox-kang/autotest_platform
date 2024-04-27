import inspect
from API.Api_action import *


class baselinegenerators:

    def __init__(self):
        self.method = Api_method()

    @allure.step("业务基线生成器页面")
    def baselinegenerators_page(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("所属协议列表")
    def protocols_all(self, filterFlag, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + filterFlag
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("协议id")
    def baselinegenerators_filter(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_protocols'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def protocols_(self, id, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + id
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("新建业务基线生成器")
    def baselinegenerators_add(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_protocols'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("使能业务基线生成器")
    def baselinegenerators_enablement_ids(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_protocols'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("禁用业务基线生成器")
    def baselinegenerators_disablement_ids(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_protocols'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除业务基线生成器")
    def baselinegenerators_generator_delete_id(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '_protocols'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

