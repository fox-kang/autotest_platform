import inspect
from API.Api_action import *


class backup:

    def __init__(self):
        self.method = Api_method()

    @allure.step("导出策略备份")
    def policies_download(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/v1.1/api/data_mgt/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

