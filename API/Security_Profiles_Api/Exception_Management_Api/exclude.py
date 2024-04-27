import inspect
from API.Api_action import *


class exclude:

    def __init__(self):
        self.method = Api_method()

    def policies_ids(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '-groupids'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("例外管理列表")
    def policies_exclude_list(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def rules_ruleFuzzyMatching(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建例外管理")
    def policies_exclude_add(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def policies_exclude_100000001(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑例外观看")
    def policies_exclude_update(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除例外管理")
    def policies_exclude_delete(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("应用例外管理")
    def policies_exclude_configuration_100000001(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()["values"]["task_id"]

    @allure.step("例外管理应用状态")
    def policies_exclude_taskstatus_(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + exclude().policies_exclude_configuration_100000001(cookie)
        max_attempts = 10  # 最大检查次数为10次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["result"]["status"]
            if statu == "ok":
                status = statu
                print("例外管理应用状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("例外管理应用状态没有在预定时间内变为ok")
        return rsp, status
