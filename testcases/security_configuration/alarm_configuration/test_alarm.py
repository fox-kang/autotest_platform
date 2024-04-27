import time

from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import Data_packet
from common.system_public import log_file, data_packet_file
from utils.logger import *
from API.Security_Profiles_Api.Alarm_Configuration_Api.alarm import *
from API.System_Management_Api.System_Log_Api.log import *
from API.Security_Profiles_Api.Intrusion_Strategy_Api.intrusion import *
from API.Threat_Detection_Api.Intrusion_Detection_Api.intrude import *
from common.security_public import *
from common.threat_public import *


@allure.feature("告警配置")
class TestAlarm:  # 告警配置

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("安全配置-告警通知配置-操作-删除")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_alarm_delete(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            data = a.read_yml_file(alarm_file)['data3']
            rsp1 = alarm().alarm_notice_add(data, cookies)
            msg1 = rsp1.json()['message']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(alarm_file)['data2']
            rsp2 = alarm().alarm_notice_list(data, cookies)
            id = rsp2.json()['result'][0]['id']
        with allure.step("执行步骤: 3"):
            values = id
            ids = ('data5', 'ids')
            replace_dict = {
                ids: [values]
            }
            data = a.replace_value_in_yml(alarm_file, replace_dict)['data5']
            rsp3 = alarm().alarm_notice_delete(data, cookies)
            msg3 = rsp3.json()['message']
            time.sleep(5)
        with allure.step('执行步骤 4'):
            end = log().time(cookies)
            start = str(int(end) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStarts = ('data1', 'timeStarts')
            replace_dict = {
                timeEnds: end,
                timeStarts: start
            }
            data = a.replace_value_in_yml(log_file, replace_dict)['data1']
            rsp4 = log().pg_logs_operationLogList(data, cookies)
            msg4 = rsp4.json()['result']['logs'][0]['message']
        self.logger.info('开始执行第{}条用例, 新增告警通知配置{}\n删除告警通知配置{}\n日志记录为{}'
                         .format(ID, msg1, msg3, msg4))
        assert msg1 == msg3

    @pytest.mark.slow("这是条测试时间较长的用例")
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('002',
                                  a.read_yml_file(data_packet_file)['K-B-ZC.pcap']),
                             ]
                             )
    @allure.story("安全配置-告警通知配置-声光报警告警功能验证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_alarm_sound(self, ID, request, cookies, pcap_data):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            data = a.read_yml_file(alarm_file)['data3']
            rsp1 = alarm().alarm_notice_add(data, cookies)
            msg1 = rsp1.json()['message']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(intrusion_file)['test']
            rsp2 = intrusion().policies(data, cookies)
            policyId = rsp2.json()['values']['policyId']
        with allure.step("执行步骤: 3"):
            rsp3, status = intrusion().policies_taskstatus_ids(cookies)
        with allure.step("执行步骤: 4"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
            time.sleep(10)
        with allure.step("执行步骤: 6"):
            values1 = intrude().time(cookies)
            values2 = str(int(values1)-86400000)
            end = ('data1', 'timeEnd')
            start = ('data1', 'timeStart')
            replacement_dict = {
                end: values1,
                start: values2
            }
            data = a.replace_value_in_yml(threat_file, replacement_dict)['data1']
            rsp6 = intrude().alerts_(data, cookies)
            rule_category = rsp6.json()['values']['result'][0]['generic']['rule_category']
        with allure.step("执行步骤: 7"):
            data = a.read_yml_file(alarm_file)['data2']
            rsp7 = alarm().alarm_notice_list(data, cookies)
            id = rsp7.json()['result'][0]['id']
        with allure.step("执行步骤: 8"):
            ids = ('data5', 'ids')
            replace_id = {
                ids: [id]
            }
            data = a.replace_value_in_yml(alarm_file, replace_id)['data5']
            rsp8 = alarm().alarm_notice_delete(data, cookies)
            msg8 = rsp8.json()['message']
        with allure.step("执行步骤: 9"):
            ids = ('data7', 'ids')
            replace_dict = {
                ids: [policyId]
            }
            data = a.replace_value_in_yml(intrusion_file, replace_dict)['data7']
            rsp9 = intrusion().policies_delete(data, cookies)
            msg9 = rsp9.json()['message']
        with allure.step("执行步骤: 10"):
            rsp10, status2 = intrusion().policies_taskstatus_ids(cookies)
        self.logger.info('开始执行第{}条用例, 新增告警通知配置:{}\n新建入侵策略id为{}\n应用入侵策略{},{}\n上传数据包{}\n数据包回放状态{}\n入侵检测数据{}\n'
                         '删除告警配置策略:{}\n删除入侵策略:{}'
                         .format(ID, msg1, policyId, status, status2, msg4, msg5, rule_category, msg8, msg9))
        assert msg1 == '操作成功' and status == status2 == 'ok' and msg5 == '触发执行数据包回放成功！'
