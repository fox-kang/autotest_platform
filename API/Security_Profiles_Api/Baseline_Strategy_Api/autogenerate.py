import inspect
from API.Api_action import *
from common.baseline_public import *


class autogenerate:  # 自学习

    def __init__(self):
        self.method = Api_method()

    @allure.step("自学习状态")
    def baseline_autogenerate_status(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        max_attempts = 10  # 最大检查次数为10次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["responseBean"]["learnStatus"]
            if statu == "finish":
                status = statu
                print("基线自学习状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("基线自学习状态没有在预定时间内变为finish")
        return rsp, status

    @allure.step("历史自学习结果")
    def baseline_autogenerate_log(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def baselinegenerators_protocols(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("开始学习")
    def baseline_autogenerate_start(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取时间戳")
    def time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp
