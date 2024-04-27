import inspect
from API.Api_action import *


class Data:

    def __init__(self):
        self.method = Api_method()

    @allure.step("数据备份")
    def get_backup_status(self, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def get_restore_status(self, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("数据配置")
    def get_data_config(self, cookie):
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("数据列表")
    def get_data_sheets(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("备份与恢复")
    def get_all_datafiles(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("保存数据配置")
    def data_config(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def backup_data(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("恢复数据")
    def restore_data(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除数据")
    def delete_datafile(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp




