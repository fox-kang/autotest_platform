import time

from API.Security_Profiles_Api.Baseline_Strategy_Api.autogenerate import autogenerate
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import Data_packet
from common.asset_public import autogenerate_file
from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.business import *
from API.System_Management_Api.System_Log_Api.log import *
from common.system_public import *
from common.baseline_public import *


@allure.feature("上行事件")
class TestAscending_event:  # 上行事件
    @pytest.mark.slow("这是条标记时间比较长的测试")
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    @pytest.mark.parametrize('ID, pcap_data, other_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['modulus_pcap'],
                                  a.read_yml_file(data_packet_file)['modbus_pcap']),
                             ]
                             )
    @pytest.mark.xfail(reason="已知问题，待修复")
    @allure.story("业务基线-上行事件-使能校验")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_business_enable_check(self, request, ID, cookies, pcap_data, other_data):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            rsp1 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp2, result2 = Data_packet().toolbox_perform_replay(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            rsp3 = autogenerate().time(cookies)
            endtime = rsp3.json()['values']['currentTime']
        with allure.step("执行步骤 4"):
            endTime = endtime
            startTime = str(int(endTime)-1800000)
            end = ('data3', 'common', 'endTime')
            start = ('data3', 'common', 'startTime')
            replacement_dict = {
                end: endTime,
                start: startTime
            }
            data = a.replace_value_in_yml(autogenerate_file, replacement_dict)['data3']
            rsp4 = autogenerate().baseline_autogenerate_start(data, cookies)
            msg4 = rsp4.json()['message']
        with allure.step("执行步骤 5"):
            rsp5, status5 = autogenerate().baseline_autogenerate_status(cookies)
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(autogenerate_file)['data1']
            rsp6 = autogenerate().baseline_autogenerate_log(data, cookies)
            msg6 = rsp6.json()['result']['list'][0]['result']
        with allure.step('执行步骤 7'):
            data = a.read_yml_file(business_file)['data6']
            rsp7 = business().baseline_business_page(data, cookies)
        with allure.step('执行步骤 8'):
            id = rsp7.json()['result']['list'][0]['id']
            status = '0'
            IDS = ('data4', 'ids')
            Status = ('data4', 'status')
            replacement_dict = {
                IDS: id,
                Status: status
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data4']
            rsp8 = business().baseline_business_enable(data, cookies)
        with allure.step("执行步骤 9"):
            rsp9, status9 = business().baseline_business_taskstatus(cookies)
        with allure.step('执行步骤 10'):
            values1 = rsp7.json()['result']['list'][0]['id']
            values2 = rsp7.json()['result']['list'][0]['pid']
            values3 = rsp7.json()['result']['list'][0]['rid']
            id = ('data5', 'id')
            rid = ('data5', 'rid')
            pid = ('data5', 'pid')
            replacement_dict = {
                id: values1,
                rid: values2,
                pid: values3
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data5']
            rsp10 = business().baseline_business_update(data, cookies)
            msg10 = rsp10.json()['message']
        with allure.step("执行步骤 11"):
            rsp11, status11 = business().baseline_business_taskstatus(cookies)
        with allure.step("执行步骤: 12"):
            rsp12 = Data_packet().toolbox_import_package(other_data['zip_file_path'], other_data['file_name'], cookies)
            msg12 = rsp12.json()["message"]
        with allure.step("执行步骤: 13"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp13, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg13 = rsp13.json()["message"]
            time.sleep(600)
        with allure.step("执行步骤: 14"):
            pass
        with allure.step('执行步骤 15'):
            values1 = rsp7.json()['result']['list'][0]['id']
            values2 = rsp7.json()['result']['list'][0]['pid']
            values3 = rsp7.json()['result']['list'][0]['rid']
            values4 = '0'
            id = ('data5', 'id')
            rid = ('data5', 'rid')
            pid = ('data5', 'pid')
            enable = ('data5', 'enable')
            replacement_dict = {
                id: values1,
                rid: values2,
                pid: values3,
                enable: values4
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data5']
            rsp15 = business().baseline_business_update(data, cookies)
            msg15 = rsp10.json()['message']
        with allure.step("执行步骤 16"):
            rsp16, status16 = business().baseline_business_taskstatus(cookies)
        with allure.step("执行步骤: 17"):
            rsp17 = Data_packet().toolbox_import_package(other_data['zip_file_path'], other_data['file_name'], cookies)
            msg17 = rsp17.json()["message"]
        with allure.step("执行步骤: 18"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp18, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg18 = rsp18.json()["message"]
        with allure.step("执行步骤: 19"):
            self.logger.info('用例第{}条执行完毕,接口返回信息为:{}\n{}\n{}\n自学习状态为:{}\n'
                             .format(ID, msg1, msg2, msg4, status5))

