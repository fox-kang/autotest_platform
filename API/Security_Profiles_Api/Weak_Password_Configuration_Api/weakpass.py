import inspect
from API.Api_action import *


class weak: # 弱口令配置
    def __init__(self):
        self.method = Api_method()

    def virusWarning_device(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("弱口令配置页面")
    def baselineConfigLog_percent(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("弱口令规则配置信息")
    def weakPass_search(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改弱口令规则配置信息")
    def weakPass_update(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("使能/禁用配置项")
    def weakPass_enable(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def weakPass_configuration(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()["values"]["task_id"]

    @allure.step("应用配置")
    def weakPass_taskstatus_(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = (Public().handle_str() + '/tsa/api/' + url_route
               + weak().weakPass_configuration(cookie))
        max_attempts = 10  # 最大检查次数为10次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["result"]["status"]
            if statu == "ok":
                status = statu
                print("应用弱口令配置状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("应用弱口令配置状态没有在预定时间内变为'ok'")
        return rsp, status
