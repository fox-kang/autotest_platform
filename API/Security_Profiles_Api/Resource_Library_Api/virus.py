import inspect
from API.Api_action import *


class Virus:

    def __init__(self):
        self.method = Api_method()

    @allure.step("病毒名称/类型")
    def virus_library_virus(self, data, path, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + path
        if path == '_type/list':
            rsp = self.method.http_get(url, None, None, cookie)
            return rsp
        else:
            rsp = self.method.http_post_json(url, data, None, None, cookie)
            return rsp
