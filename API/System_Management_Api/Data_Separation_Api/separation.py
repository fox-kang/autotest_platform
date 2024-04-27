import inspect
from API.Api_action import *


class separation:

    def __init__(self):
        self.method = Api_method()

    @allure.step("数据分离列表")
    def disks_info(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

