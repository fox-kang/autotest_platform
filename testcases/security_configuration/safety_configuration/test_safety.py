import time

from API.Security_Profiles_Api.Safety_Margin_Api.outreach import *
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from API.Threat_Detection_Api.Security_Zone_Alarm_Api.domain import *
from common.security_public import *
from common.system_public import *
from common.threat_public import *
from utils.logger import get_log


@allure.feature("安全域")
class TestSafety:  # 安全域

    @pytest.mark.slow("这是条测试时间较长的用例")
    # @pytest.mark.flaky(reruns=1, reruns_delay=60)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['AB_EthernetIP_CIP_pcap']),
                             ]
                             )
    @allure.story("新建安全域-违规外联-验证多个安全域内ip违规外联的功能")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_safety_Illegal_outreach(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(outreach_file)['data2']
            rsp1 = outreach().device_outreach_intranet_update(data, cookies)
            msg1 = rsp1.json()['message']
        with allure.step("执行步骤 2"):
            data = a.read_yml_file(outreach_file)['data4']
            rsp2 = outreach().device_outreach_partition_add(data, cookies)
            partitionId = rsp2.json()['values']['partitionId']
        with allure.step("执行步骤 3"):
            values1 = partitionId
            values2 = 'false'
            values3 = 'high'
            partitionIdS = ('data7', 'partitionId')
            isContainLink = ('data7', 'isContainLink')
            severity = ('data7', 'severity')
            replace_dict = {
                partitionIdS: values1,
                isContainLink: values2,
                severity: values3
            }
            data = a.replace_value_in_yml(outreach_file, replace_dict)['data7']
            rsp3 = outreach().device_outreach_partition_config_(data, cookies)
            msg3 = rsp3.json()['message']
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(outreach_file)['data10']
            rsp4, status1 = outreach().device_outreach_configuration_taskstatus_(data, cookies)
            time.sleep(10)
        with allure.step("执行步骤: 5"):
            rsp5 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp6, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg6 = rsp6.json()["message"]
        with allure.step("执行步骤: 7"):
            endtime = domain().time(cookies)
            starttime = str(int(endtime)-300000)
            alarm = '6'
            alarmType = ('data1', 'alarmType')
            endTime = ('data1', 'endTime')
            startTime = ('data1', 'startTime')
            replace_dict = {
                endTime: endtime,
                alarmType: alarm,
                startTime: starttime
            }
            data = a.replace_value_in_yml(domain_file, replace_dict)['data1']
            rsp7 = domain().alerts_(data, cookies)
            src_ip = rsp7.json()['values']['result'][0]['generic']['src_ip']
            description = rsp7.json()['values']['result'][0]['generic']['description']
        with allure.step("执行步骤 8"):
            values = partitionId
            ids = ('data9', 'ids')
            replace_dict = {
                ids: [values]
            }
            data = a.replace_value_in_yml(outreach_file, replace_dict)['data9']
            rsp9 = outreach().device_outreach_partition_delete(data, cookies)
            msg9 = rsp9.json()['message']
        with allure.step("执行步骤 9"):
            data = a.read_yml_file(outreach_file)['data10']
            rsp10, status2 = outreach().device_outreach_configuration_taskstatus_(data, cookies)
        self.logger.info(
            '开始执行第{}条用例,内网配置编辑{}\n新建安全域id为{}\n新建安全域{}\n应用安全域状态为{},{}\n'
            '上传数据包状态为{}\n回放数据包状态为{}\n违规外联新增告警列表ip为{}\n告警描述为{}\n删除安全域{}'
            .format(ID, msg1, partitionId, msg3, status1, status2, msg5, msg6, src_ip, description, msg9))
        assert status1 == status2 == 'ok' and description == '违规外联'

    @pytest.mark.slow("这是条测试时间较长的用例")
    # @pytest.mark.flaky(reruns=1, reruns_delay=60)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('002',
                                  a.read_yml_file(data_packet_file)['AB_EthernetIP_CIP_pcap']),
                             ]
                             )
    @allure.story("新建安全域-违规跨区互联-验证多个安全域违规跨区互联功能")
    def test_safety_Inter_regional_interconnection(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            time.sleep(10)
            data = a.read_yml_file(outreach_file)['data2']
            rsp1 = outreach().device_outreach_intranet_update(data, cookies)
            msg1 = rsp1.json()['message']
        with allure.step("执行步骤 2"):
            values1 = '192.168.0.5-192.168.0.15'
            values2 = 'IPv4'
            addr = ('data4', 'addrRange', 0, 'addr')
            type = ('data4', 'addrRange', 0, 'type')
            replace_dict = {
                addr: values1,
                type: values2
            }
            data = a.replace_value_in_yml(outreach_file, replace_dict)['data4']
            rsp2 = outreach().device_outreach_partition_add(data, cookies)
            partitionId = rsp2.json()['values']['partitionId']
        with allure.step("执行步骤 3"):
            values1 = partitionId
            values2 = 'false'
            values3 = 'high'
            values4 = '1'
            partitionIdS = ('data7', 'partitionId')
            isContainLink = ('data7', 'isContainLink')
            severity = ('data7', 'severity')
            connectionType = ('data7', 'connectionType')
            replace_dict = {
                partitionIdS: values1,
                isContainLink: values2,
                severity: values3,
                connectionType: values4
            }
            data = a.replace_value_in_yml(outreach_file, replace_dict)['data7']
            rsp3 = outreach().device_outreach_partition_config_(data, cookies)
            msg3 = rsp3.json()['message']
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(outreach_file)['data10']
            rsp4, status1 = outreach().device_outreach_configuration_taskstatus_(data, cookies)
            time.sleep(10)
        with allure.step("执行步骤: 5"):
            rsp5 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp6, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg6 = rsp6.json()["message"]
        with allure.step("执行步骤: 7"):
            endtime = domain().time(cookies)
            starttime = str(int(endtime)-300000)
            alarm = '7'
            alarmType = ('data1', 'alarmType')
            endTime = ('data1', 'endTime')
            startTime = ('data1', 'startTime')
            replace_dict = {
                endTime: endtime,
                alarmType: alarm,
                startTime: starttime
            }
            data = a.replace_value_in_yml(domain_file, replace_dict)['data1']
            rsp7 = domain().alerts_(data, cookies)
            src_ip = rsp7.json()['values']['result'][0]['generic']['src_ip']
            description = rsp7.json()['values']['result'][0]['generic']['description']
            alert_severity = rsp7.json()['values']['result'][0]['generic']['alert_severity']
        with allure.step("执行步骤 8"):
            values = partitionId
            ids = ('data9', 'ids')
            replace_dict = {
                ids: [values]
            }
            data = a.replace_value_in_yml(outreach_file, replace_dict)['data9']
            rsp9 = outreach().device_outreach_partition_delete(data, cookies)
            msg9 = rsp9.json()['message']
        with allure.step("执行步骤 9"):
            data = a.read_yml_file(outreach_file)['data10']
            rsp10, status2 = outreach().device_outreach_configuration_taskstatus_(data, cookies)
        self.logger.info(
            '开始执行第{}条用例,内网配置编辑{}\n新建安全域id为{}\n新建安全域{}\n应用安全域状态为{},{}\n'
            '上传数据包状态为{}\n回放数据包状态为{}\n跨区互联新增告警列表ip为{}\n告警描述为{}\n删除安全域{}'
            .format(ID, msg1, partitionId, msg3, status1, status2, msg5, msg6, src_ip, description, msg9))
        assert status1 == status2 == 'ok' and description == '违规跨区互联' and alert_severity == 'high'

