import inspect
from API.Api_action import *


class outreach:

    def __init__(self):
        self.method = Api_method()

    def virusWarning_device(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("安全域列表")
    def device_outreach_partition_list(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def device_outreach_intranet_get(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '?deviceId=100000001'
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改内网配置")
    def device_outreach_intranet_update(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("保存安全域")
    def device_outreach_ipJudgment(self, data, cookie):  # 3 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建安全域")
    def device_outreach_partition_add(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def protocols(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("确定新建安全域")
    def device_outreach_partition_config_(self, data, cookie):  # 7
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + 'add_or_update'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("修改安全域使能状态")
    def device_outreach_change(self, data, cookie):  # 8
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '-status'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除安全域")
    def device_outreach_partition_delete(self, data, cookie):  # 9
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def device_outreach_configuration_(self, data, cookie): # 10
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()['values']['task_id']

    def device_outreach_configuration_taskstatus_(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + outreach().device_outreach_configuration_(data, cookie)
        max_attempts = 10  # 最大检查次数为10次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["result"]["status"]
            if statu == "ok":
                status = statu
                print("应用安全域配置状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("应用安全域配置状态没有在预定时间内变为'ok'")
        return rsp, status
