import inspect
from API.Api_action import *
from common.login_public import *


class business:

    def __init__(self):
        self.method = Api_method()

    @allure.step("新建业务基线")
    def protocols_all(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '?filterFlag=true'
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("新建业务基线特征")
    def protocols(self, num, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + '/' + num + '/fields'
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("确定新建业务基线")
    def baseline_business_add(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("批量使能业务基线")
    def baseline_business_enable(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("批量删除业务基线")
    def baseline_business_delete(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def baseline_business_configuration_100000001(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp.json()['values']['task_id']

    @allure.step("应用业务基线")
    def baseline_business_taskstatus(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = (Public().handle_str() + '/tsa/api/' + url_route + '/'
               + business().baseline_business_configuration_100000001(cookie))
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

    @allure.step("编辑业务基线")
    def baseline_business_update(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("业务基线页面")
    def baseline_business_page(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
