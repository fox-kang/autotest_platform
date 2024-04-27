import allure

from API.Security_Profiles_Api.Baseline_Strategy_Api.autogenerate import autogenerate
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import Data_packet
from common.asset_public import autogenerate_file
from common.system_public import data_packet_file
from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.flow import *
from common.baseline_public import *
from communicate.ssh import *


@allure.feature("流量基线")
class TestNewFlowBaseline:  # 流量基线

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.file_path(flow_file)
    @pytest.mark.parametrize('ID, mac_index', [('001', [1])])
    @allure.story("新建流量基线编辑并下发")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_flow(self, request, ID, cookies, mac_to_yaml, mac_index, random_mac):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(flow_file)['data1']
            rsp1 = flow().baseline_flow(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step('执行步骤 2'):
            data = a.read_yml_file(flow_file)['data2']
            rsp2 = flow().baseline_flow_filter(data, cookies)
        with allure.step('执行步骤 3'):
            values = rsp2.json()['values']['pageBean']['list'][0]['id']
            id = ('data7', 'id')
            dst_mac = ('data7', 'dst_mac')
            src_mac = ('data7', 'src_mac')
            replacement_dict = {
                id: values,
                dst_mac: random_mac,
                src_mac: random_mac
            }
            data = a.replace_value_in_yml(flow_file, replacement_dict)['data7']
            rsp3 = flow().baseline_flow_update(data, cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            rsp4, status = flow().baseline_flow_taskstatus(cookies)
            msg4 = rsp4.json()["message"]
        self.logger.info('用例{}执行完毕,接口返回信息为{},{},{},mac地址为{}'.format(ID, msg1, msg3, msg4, random_mac))
        assert msg1 == "操作成功" and msg3 == "操作成功" and status == 'ok'

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("删除流量基线并应用")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete_flow(self, request, ID, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(flow_file)['data2']
            rsp1 = flow().baseline_flow_filter(data, cookies)
            msg1 = rsp1.json()['values']['pageBean']['list'][0]['id']
        with allure.step("执行步骤 2"):
            id = ('data6', 'ids')
            replacement_dict = {
                id: [msg1]
            }
            data = a.replace_value_in_yml(flow_file, replacement_dict)['data6']
            rsp2 = flow().baseline_flow_delete(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            rsp3, status = flow().baseline_flow_taskstatus(cookies)
        self.logger.info('用例{}执行完毕，接口返回信息为{},{},基线应用状态为{}'.format(ID, msg1, msg2, status))
        assert (msg2 == '操作成功' and status == 'ok')

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('003',
                                  a.read_yml_file(data_packet_file)['946_pcap']),
                             ]
                             )
    @pytest.mark.xfail(reason="已知问题，待修复")
    @allure.story("新建自学习-流量基线")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_new_self_learning(self, request, ID, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            rsp1 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp2, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            rsp3 = autogenerate().time(cookies)
            endtime = rsp3.json()['values']['currentTime']
        with allure.step("执行步骤 4"):
            endTime = endtime
            startTime = str(int(endTime)-1800000)
            end = ('data2', 'common', 'endTime')
            start = ('data2', 'common', 'startTime')
            replacement_dict = {
                end: endTime,
                start: startTime
            }
            data = a.replace_value_in_yml(autogenerate_file, replacement_dict)['data2']
            rsp4 = autogenerate().baseline_autogenerate_start(data, cookies)
            msg4 = rsp4.json()['message']
        with allure.step("执行步骤 5"):
            rsp5 = autogenerate().baseline_autogenerate_status(cookies)
            msg5 = rsp5.json()['values']['responseBean']['learnStatus']
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(autogenerate_file)['data1']
            rsp6 = autogenerate().baseline_autogenerate_log(data, cookies)
            msg6 = rsp6.json()['result']['list'][0]['result']

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('004',
                                  a.read_yml_file(data_packet_file)['modbus_02_pcap']),
                             ]
                             )
    @pytest.mark.xfail(reason="已知问题，待修复")
    @allure.story("编辑基线-安全事件触发验证-编辑后未应用下发")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_update_flow_safety(self, request, ID, cookies, pcap_data):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(flow_file)['data8']
            rsp1 = flow().baseline_flow(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            rsp2, status = flow().baseline_flow_taskstatus(cookies)
        with allure.step("执行步骤 3"):
            rsp3 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            rsp4 = SSH().ssh('10.0.8.6', '10022', 'rayleigh', 'Silvers$R7',
                             'sudo tcpreplay -i veth-taa-0 -x 100 -l 1 /home/data_package/modbus_tcp_02.pcap')

