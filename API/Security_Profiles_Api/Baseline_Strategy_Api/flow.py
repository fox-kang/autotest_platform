import inspect
from API.Api_action import *
from common.login_public import *


class flow:

    def __init__(self):
        self.method = Api_method()

    @allure.step("新建流量基线")
    def baseline_flow(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def baseline_flow_configuration_100000001(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()['values']['task_id']

    @allure.step("应用流量基线")
    def baseline_flow_taskstatus(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = (Public().handle_str() + '/tsa/api/' + url_route + '/'
               + flow().baseline_flow_configuration_100000001(cookie))
        max_attempts = 10  # 最大检查次数为10次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["result"]["status"]
            if statu == "ok":
                status = statu
                print("应用基线状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("应用基线状态没有在预定时间内变为'ok'")
        return rsp, status

    @allure.step("流量基线列表")
    def baseline_flow_filter(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("批量告警设置流量基线")
    def baseline_flow_updateConfig(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("批量使能流量基线")
    def baseline_flow_enable(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("批量禁用流量基线")
    def baseline_flow_disable(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除流量基线")
    def baseline_flow_delete(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑流量基线")
    def baseline_flow_update(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
