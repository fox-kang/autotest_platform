from API.Api_action import *
from common.login_public import *

cookies = Public().cookie()


class Login:

    def __init__(self):
        self.method = Api_method()

    def login(self):
        url = Public().login_str()
        staticVCode, Cookie = Public().get_code()
        data = {"username": a.read_yml_file(config)['username'], "password": Public().password(Cookie),
                "staticVCode": staticVCode}
        head = {"Cookie": Cookie}
        rsp = self.method.http_post_data(url, data, head, None)
        return rsp

