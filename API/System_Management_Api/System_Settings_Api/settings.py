import inspect
from API.Api_action import *


class settings:

    def __init__(self):
        self.method = Api_method()

    @allure.step("编辑SSH远程登录")
    def ssh_status_update(self, running, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + running
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def time_(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def software_timezone_get_time(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def time_clocksource_param(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("登录保护设置")
    def restriction(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("登录超时时间设置")
    def sys_changeoverduetime(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("多因子认证")
    def sys_getoverduetime(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("登录密码设置")
    def restriction_password(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/' + url_route + '_check'
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑邮箱推送信息")
    def systememails_update(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    def systememails(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑告警邮箱推送状态")
    def systememails_enable(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("刷新STMP服务器地址")
    def systememails_test(self, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("编辑手机短信推送")
    def system_sms_codeList(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑手机短信推送状态")
    def system_sms_enable(self, data, cookie):  # 7
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑可信任ip")
    def iprule(self, data, cookie):  # 8
        url_route = inspect.currentframe().f_code.co_name
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑流量下载服务")
    def toolbox_flow_toggleStatus(self, data, cookie):  # 9
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑SNMP服务设置")
    def snmp_config(self, data, cookie):  # 10
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("添加审计目标")
    def taafilter_addPolicy(self, data, cookie):  # 11
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除审计目标")
    def taafilter_deletePolicy(self, data, cookie):  # 12
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("获取审计目标信息")
    def taafilter_getPolicyConfig(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("编辑自动扫描")
    def automaticScan_config(self, data, cookie):  # 13
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新建服务器设置")
    def transmit_add(self, data, cookie):  # 14
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/data_' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑服务器设置")
    def transmit_update(self, data, cookie):  # 15
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/data_' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除服务器设置")
    def transmit_delete(self, data, cookie):  # 16
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/data_' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("服务器设置列表")
    def transmit_list(self, data, cookie):  # 17
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/data_' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp
