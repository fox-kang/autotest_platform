import time

from utils.logger import *
from API.Security_Profiles_Api.Intrusion_Strategy_Api.i_rule_template import *
from API.Security_Profiles_Api.Intrusion_Strategy_Api.intrusion import *
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from API.Threat_Detection_Api.Intrusion_Detection_Api.intrude import *
from API.Flow_Analysis_Api.Behavior_Audit_Api.audits import *
from common.security_public import *
from common.system_public import *
from common.threat_public import *
from common.flow_public import *


@allure.feature("入侵检测")
class TestIntrusion:  # 入侵检测

    @pytest.mark.slow("这是条测试时间较长的用例")
    # @pytest.mark.flaky(reruns=1, reruns_delay=60)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['intrude_pcap']),
                             ]
                             )
    @allure.story("入侵策略功能验证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_intrude(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            data = a.read_yml_file(intrusion_file)['data2']
            rsp = intrusion().policies_page(data, cookies)
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(rules_file)['data2']
            rsp9 = rules().templates_page(data, cookies)
            tempid = rsp9.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 3"):
            templateId = ('data4', 'templateId')
            replace_dict = {
                templateId: tempid
            }
            data = a.replace_value_in_yml(rules_file, replace_dict)['data4']
            rsp10 = rules().rules_page(data, cookies)
            rule_id = rsp10.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 4"):
            id = ('data9', 'id')
            replace_dict = {
                id: rule_id
            }
            data = a.replace_value_in_yml(rules_file, replace_dict)['data9']
            rsp1 = rules().rules_update(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤: 5"):
            data1 = a.read_yml_file(intrusion_file)['data5']
            values1 = rsp.json()['result']['list'][0]['id']
            values2 = rsp.json()['result']['list'][0]['name']
            id = ('data9', 'id')
            name = ('data9', 'name')
            replacement_dict = {
                id: values1,
                name: values2
            }
            data2 = a.replace_value_in_yml(intrusion_file, replacement_dict)['data9']
            rsp2 = intrusion().templates_page(data1, cookies)
            rsp3 = intrusion().policies_update(data2, cookies)
            msg2 = rsp2.json()["message"]
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤: 6"):
            rsp4, status = intrusion().policies_taskstatus_ids(cookies)
            time.sleep(30)
        with allure.step("执行步骤: 7"):
            rsp5 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 8"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp6, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg6 = rsp6.json()["message"]
        with allure.step("执行步骤: 9"):
            rsp7 = intrude().alerts_getPolicyRuleType_1(cookies)
            msg7 = rsp7.json()["result"][0]["type"]
        with allure.step("执行步骤: 8"):
            values1 = audits().time(cookies)
            values2 = str(int(values1)-2800000)
            end = ('data1', 'timeEnd')
            start = ('data1', 'timeStart')
            replacement_dict = {
                end: values1,
                start: values2
            }
            data = a.replace_value_in_yml(audits_file, replacement_dict)['data1']
            rsp8 = audits().audits_taa_pagesss(data, cookies)
            msg8 = rsp8.json()['values']['list'][0]['generic']['protocol']
            try:
                msg8 = rsp8.json()['values']['list'][0]['generic']['protocol']
            except IndexError:
                print('页面无数据')
            except Exception as e:
                print(f'发生异常：{e}')
        self.logger.info(
            '开始执行第{}条用例,参数为{},接口返回信息为{}\n{}\n{}\n{}\n{}\n{},通信协议类型为{},回放状态在预定时间内变为{},入侵攻击类型为{}'
            .format(ID, pcap_data, msg1, msg2, msg3, status, msg5, msg6, msg8, result, msg7))
        assert msg1 == "操作成功" and msg6 == "触发执行数据包回放成功！" and result == "success" and msg7 == "RPC攻击"

    @pytest.mark.smoke('这是一条冒烟用例')
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("新建入侵策略")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_intrusion(self, request, ID, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            values = random_string
            name = ('data6', 'name')
            replacement_dict = {
                name: values
            }
            data1 = a.replace_value_in_yml(intrusion_file, replacement_dict)['data6']
            rsp1 = intrusion().policies(data1, cookies)
            msg1 = rsp1.json()['values']['policyId']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(intrusion_file)['data2']
            rsp2 = intrusion().policies_page(data, cookies)
            msg2 = rsp2.json()['result']['list'][0]['name']
        with allure.step("执行步骤: 3"):
            rsp3, status = intrusion().policies_taskstatus_ids(cookies)
        self.logger.info(
            '开始执行第{}条用例,参数为{},创建策略名称为{},接口返回信息为{},应用策略状态为{}'.format(ID, msg1, values, msg1, status))
        assert msg2 == values and status == 'ok'

