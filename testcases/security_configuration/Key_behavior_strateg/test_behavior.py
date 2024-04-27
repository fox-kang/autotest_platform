import time

from utils.logger import *
from API.Security_Profiles_Api.Key_Behavior_Strategy_Api.behavior import *
from API.Security_Profiles_Api.Key_Behavior_Strategy_Api.b_rule_template import *
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from API.Flow_Analysis_Api.Behavior_Audit_Api.audits import *
from common.security_public import *
from common.system_public import *
from common.flow_public import *


@allure.feature("关键行为策略")
class TestKey_behavior:
    @pytest.mark.smoke('这是一条冒烟用例')
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['behavior_pcap']),
                             ]
                             )
    @allure.story("检测关键行为策略功能")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_behavior(self, request, ID, pcap_data, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            values = random_string
            name = ('data5', 'name')
            replacement_dict = {
                name: values
            }
            data1 = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data5']
            rsp1 = behavior().policies(data1, cookies)
            msg1 = rsp1.json()['values']['policyId']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(key_behavior_file)['data2']
            rsp2 = behavior().policies_page(data, cookies)
            msg2 = rsp2.json()['result']['list'][0]['name']
            ids = rsp2.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 3"):
            rsp3, status1 = behavior().policies_taskstatus(cookies)
            time.sleep(30)
        with allure.step("执行步骤: 4"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            values1 = audits().time(cookies)
            values2 = str(int(values1) - 86400000)
            end = ('data2', 'endTime')
            start = ('data2', 'startTime')
            replacement_dict = {
                end: values1,
                start: values2
            }
            data = a.replace_value_in_yml(audits_file, replacement_dict)['data2']
            rsp6 = audits().filter_match_protocols(data, cookies)
            msg6 = rsp6.json()['result']
        with allure.step("执行步骤: 7"):
            values3 = [ids]
            id = ('data7', 'ids')
            replacement_dict = {
                id: values3
            }
            data = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data7']
            rsp7 = behavior().policies_delete(data, cookies)
            msg7 = rsp7.json()["message"]
        with allure.step("执行步骤: 8"):
            rsp8, status2 = behavior().policies_taskstatus(cookies)
        self.logger.info(
            '开始执行第{}条用例\n参数为{}\n创建策略名称为{}\n接口返回信息为{},{},{}\n应用策略状态为{}\n通信协议为{}'
            .format(ID, data1, values, msg1, msg4, msg7, status1, msg6))
        assert msg2 == values and status1 == 'ok' and msg5 == '触发执行数据包回放成功！' and status2 == 'ok'

    @pytest.mark.slow('这是一条标记时间比较长的测试')
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('002',
                                  a.read_yml_file(data_packet_file)['modbus_02_pcap']),
                             ]
                             )
    @allure.story("关键行为策略-功能-告警类型")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_alert_type(self, request, ID, pcap_data, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 前置"):
            data = a.read_yml_file(rule_template_file)['data2']
            rsp12 = rule().templates_page(data, cookies)
            id = rsp12.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 1"):
            templateId = ('data8', 'templateId')
            name = ('data8', 'name')
            replace = {
                templateId: id,
                name: random_string
            }
            data = a.replace_value_in_yml(rule_template_file, replace)['data8']
            rsp1 = rule().rules_add(data, cookies)
            ruleId = rsp1.json()['values']['ruleId']
        with allure.step("执行步骤: 2"):
            templateIdsStr = ('data5', 'templateIdsStr')
            name = ('data5', 'name')
            replacement_dict = {
                templateIdsStr: id,
                name: random_string
            }
            data = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data5']
            rsp2 = behavior().policies(data, cookies)
            msg2 = rsp2.json()['values']['policyId']
        with allure.step("执行步骤: 3"):
            rsp3, status1 = behavior().policies_taskstatus(cookies)
            time.sleep(30)
        with allure.step("执行步骤: 4"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            values1 = audits().time(cookies)
            values2 = str(int(values1) - 86400000)
            end = ('data4', 'endTime')
            start = ('data4', 'startTime')
            replacement_dict = {
                end: values1,
                start: values2
            }
            data = a.replace_value_in_yml(audits_file, replacement_dict)['data4']
            rsp6 = audits().alerts_(data, cookies)
            rule_category = rsp6.json()['values']['result'][0]['generic']['rule_category']
        with allure.step("执行步骤: 7"):
            templateId = ('data4', 'templateId')
            replace = {
                templateId: id
            }
            data = a.replace_value_in_yml(rule_template_file, replace)['data4']
            rsp7 = rule().rules_page(data, cookies)
            id1 = rsp7.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 8"):
            values3 = id1
            ids = ('data10', 'ids')
            replacement_dict = {
                ids: [values3]
            }
            data = a.replace_value_in_yml(rule_template_file, replacement_dict)['data10']
            rsp8 = rule().rules_delete_idstr(data, cookies)
            msg8 = rsp8.json()['message']
        with allure.step("执行步骤: 9"):
            data = a.read_yml_file(key_behavior_file)['data2']
            rsp9 = behavior().policies_page(data, cookies)
            ID = rsp9.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 10"):
            values4 = ID
            ids = ('data7', 'ids')
            replacement_dict = {
                ids: [values4]
            }
            data = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data7']
            rsp10 = behavior().policies_delete(data, cookies)
            msg10 = rsp10.json()['message']
        with allure.step("执行步骤: 11"):
            rsp11, status2 = behavior().policies_taskstatus(cookies)
            time.sleep(30)
        self.logger.info(
            '开始执行第{}条用例\n新建规则模版id为{}\n新建关键行为策略id为{}\n告警类型为{}\n关键行为策略应用状态为{},{}\n数据包上传状态为{}\n数据包回放状态为{}'
            .format(ID, ruleId, msg2, rule_category, status1, status2, msg4, msg5))
        assert msg8 == '操作成功' and status1 == 'ok' and msg5 == '触发执行数据包回放成功！' and status2 == 'ok' and msg10 == '操作成功'

    @pytest.mark.slow('这是一条标记时间比较长的测试')
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('003',
                                  a.read_yml_file(data_packet_file)['modbus_pcap']),
                             ]
                             )
    @allure.story("关键行为策略-功能-告警级别")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_alert_level(self, request, ID, pcap_data, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 前置"):
            data = a.read_yml_file(rule_template_file)['data2']
            rsp12 = rule().templates_page(data, cookies)
            id = rsp12.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 1"):
            values = '4'
            templateId = ('data8', 'templateId')
            severity_id = ('data8', 'severity_id')
            name = ('data8', 'name')
            replacement_dict = {
                severity_id: values,
                templateId: id,
                name: random_string
            }
            data = a.replace_value_in_yml(rule_template_file, replacement_dict)['data8']
            rsp1 = rule().rules_add(data, cookies)
            ruleId = rsp1.json()['values']['ruleId']
        with allure.step("执行步骤: 2"):
            name = ('data5', 'name')
            templateIdsStr = ('data5', 'templateIdsStr')
            replacement_dict = {
                name: random_string,
                templateIdsStr: id
            }
            data = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data5']
            rsp2 = behavior().policies(data, cookies)
            msg2 = rsp2.json()['values']['policyId']
        with allure.step("执行步骤: 3"):
            rsp3, status1 = behavior().policies_taskstatus(cookies)
            time.sleep(30)
        with allure.step("执行步骤: 4"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            values1 = audits().time(cookies)
            values2 = str(int(values1) - 86400000)
            end = ('data4', 'endTime')
            start = ('data4', 'startTime')
            replacement_dict = {
                end: values1,
                start: values2
            }
            data = a.replace_value_in_yml(audits_file, replacement_dict)['data4']
            rsp6 = audits().alerts_(data, cookies)
            alert_severity1 = rsp6.json()['values']['result'][0]['generic']['alert_severity']
        with allure.step("执行步骤: 6.5"):
            templateId = ('data4', 'templateId')
            replacement_dict = {
                templateId: id
            }
            data = a.replace_value_in_yml(rule_template_file, replacement_dict)['data4']
            rsp0 = rule().rules_page(data, cookies)
            id1 = rsp0.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 7"):
            values = '3'
            values0 = id1
            templateId = ('data8', 'templateId')
            severity_id = ('data8', 'severity_id')
            name = ('data8', 'name')
            id2 = ('data8', 'id')
            replacement_dict = {severity_id: values,
                                id2: values0,
                                templateId: id,
                                name: random_string}
            data = a.replace_value_in_yml(rule_template_file, replacement_dict)['data8']
            rsp7 = rule().rules_update(data, cookies)
            msg7 = rsp7.json()['message']
        with allure.step("执行步骤: 8"):
            rsp8, status2 = behavior().policies_taskstatus(cookies)
            time.sleep(30)
        with allure.step("执行步骤: 9"):
            rsp9 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg9 = rsp9.json()["message"]
        with allure.step("执行步骤: 10"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp10, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg10 = rsp10.json()["message"]
        with allure.step("执行步骤: 11"):
            values3 = audits().time(cookies)
            values4 = str(int(values1) - 86400000)
            end = ('data4', 'endTime')
            start = ('data4', 'startTime')
            replacement_dict = {
                end: values3,
                start: values4
            }
            data = a.replace_value_in_yml(audits_file, replacement_dict)['data4']
            rsp11 = audits().alerts_(data, cookies)
            alert_severity2 = rsp11.json()['values']['result'][0]['generic']['alert_severity']
        with allure.step("执行步骤: 12"):
            templateId = ('data4', 'templateId')
            replace = {
                templateId: id
            }
            data = a.replace_value_in_yml(rule_template_file, replace)['data4']
            rsp12 = rule().rules_page(data, cookies)
            id3 = rsp12.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 13"):
            values5 = id3
            ids = ('data10', 'ids')
            replacement_dict = {
                ids: [values5]
            }
            data = a.replace_value_in_yml(rule_template_file, replacement_dict)['data10']
            rsp13 = rule().rules_delete_idstr(data, cookies)
            msg13 = rsp13.json()['message']
        with allure.step("执行步骤: 14"):
            data = a.read_yml_file(key_behavior_file)['data2']
            rsp14 = behavior().policies_page(data, cookies)
            ID = rsp14.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 15"):
            values6 = ID
            ids = ('data7', 'ids')
            replacement_dict = {
                ids: [values6]
            }
            data = a.replace_value_in_yml(key_behavior_file, replacement_dict)['data7']
            rsp15 = behavior().policies_delete(data, cookies)
            msg15 = rsp15.json()['message']
        with allure.step("执行步骤: 16"):
            rsp16, status3 = behavior().policies_taskstatus(cookies)
        self.logger.info(
            '开始执行第{}条用例\n新建规则模版id为{}\n新建关键行为策略id为{}\n告警级别为{}\n{}\n应用关键行为策略状态为{},{},{}'
            .format(ID, ruleId, msg2, alert_severity1, alert_severity2, status1, status2, status3))
        assert (alert_severity1 == 'critical'
                and alert_severity2 == 'high'
                and msg5 == '触发执行数据包回放成功！'
                and msg10 == '触发执行数据包回放成功！'
                and msg4 == '操作成功'
                and msg7 == '操作成功'
                and msg9 == '操作成功'
                and msg13 == '操作成功'
                and msg15 == '操作成功')
