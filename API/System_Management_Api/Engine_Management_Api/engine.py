import inspect
import time
from API.Api_action import *


class engine:  # 引擎管理

    def __init__(self):
        self.method = Api_method()

    @allure.step("引擎设备管理列表")
    def devices_pagination(self, data, cookie):  # 1
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("引擎设备管理类型")
    def devices_types(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("引擎设备采集协议列表")
    def protocols_all(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    @allure.step("引擎设备关联病毒列表")
    def antivirus_template_getAll(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, None, None, None, cookie)
        return rsp

    def organasset_networkaddress_getAllType(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    def organasset_extendattribute_getAllDataType(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("引擎设备状态")
    def devices_monitor_status(self, data, cookie):  # 2
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("新增引擎设备")
    def devices_add(self, data, cookie):  # 3
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑引擎设备")
    def devices_update(self, data, cookie):  # 4
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("编辑引擎设备状态")
    def devices_enable(self, data, cookie):  # 5
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("引擎设备状态监测")
    def zabbix_item_cpu(self, host, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + host
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("自身性能")
    def zabbix_item_JITData(self, host, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + host
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("引擎设备监测阈值设置")
    def dashboards_system_alarm_getTriggerByHost(self, host, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + host
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改监测阈值")
    def dashboards_system_alarm_triggerByHostAndHWName(self, data, cookie):  # 6
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("引擎设备下载配置")
    def devices_download_config_(self, id, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + id
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("引擎设备回读安全策略")
    def policy_readBack_startMission(self, data, cookie):  # 7
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()["values"]["taskId"]

    @allure.step("引擎设备回读状态")
    def policy_readBack_process(self, taskId, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/' + url_route + taskId
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("异常链路告警设置")
    def baseline_link_violation_get(self, violationlLink, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + violationlLink
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("修改异常链路告警设置")
    def baseline_link_violation_modify(self, data, cookie):  # 8
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp

    @allure.step("删除引擎设备")
    def devices_delete_batch_force_idstr(self, data, cookie):  # 9
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()["values"]["taskId"]

    def devices_configuration(self, data, cookie):  # 10
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        return rsp.json()["values"]["task_id"]

    @allure.step("应用引擎")
    def devices_taskstatus_(self, data, cookie):  # 10
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + engine().devices_configuration(data, cookie)
        max_attempts = 10  # 最大检查次数为5次
        interval = 3  # 每隔5秒检查一次
        for _ in range(max_attempts):
            rsp = self.method.http_get(url, None, None, cookie)
            statu = rsp.json()["values"]["result"]["status"]
            if statu == "ok":
                status = statu
                print("应用引擎状态在预定时间内变为{}".format(status))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("应用引擎状态没有在预定时间内变为'ok'")
        return rsp, status

    def devices_deletetaskstatus_(self, taskID, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route + taskID
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp
