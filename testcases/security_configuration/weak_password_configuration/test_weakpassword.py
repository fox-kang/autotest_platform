import time

from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from API.System_Management_Api.Tool_Box_Api.ping import *
from utils.logger import *
from API.Security_Profiles_Api.Weak_Password_Configuration_Api.weakpass import *
from API.Vulnerability_Api.Weak_Password_Api.weak import *
from common.security_public import *
from common.system_public import *
from common.vulnerability_public import *


@allure.feature("弱口令配置")
class TestWeak_password:  # 弱口令配置

    @pytest.mark.slow("这是条测试时间较长的用例")
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['weak_pcap']),
                             ]
                             )
    @allure.story("弱口令配置功能验证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_weak(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(weak_password_file)['data2']
            rsp1 = weak().weakPass_update(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            rsp2, status = weak().weakPass_taskstatus_(cookies)
            time.sleep(30)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 2"):
            rsp6 = ping().system_role(cookies)
            msg6 = rsp6.json()['message']
        with allure.step("执行步骤: 3"):
            rsp3 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤: 4"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp4, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            values1 = weakness().time(cookies)  # 获取访问页面时的时间戳
            values2 = str(int(values1)-300000)
            timeEnds = ('data2', 'endTime')
            startTime = ('data2', 'startTime')
            replacement_dict = {
                timeEnds: values1,
                startTime: values2
            }
            data = a.replace_value_in_yml(weak_file, replacement_dict)['data2']
            rsp5 = weakness().weakPass_list(data, cookies)
            msg5 = rsp5.json()["values"]["list"][0]["weakPassword"]
            try:
                msg5 = rsp5.json()["values"]["list"][0]["weakPassword"]
            except IndexError:
                print('不存在与该index匹配的键')
            except Exception as E:
                print(f'发生异常:{E}')
        self.logger.info(
            '开始执行第{}条用例,参数为{},访问页面时间戳为{},接口返回信息为{},{},{},{},{},{},回放状态在预定时间内变为{},弱口令配置应用状态为{}'
            .format(ID, pcap_data, values1, msg1, msg2, msg3, msg4, msg5, msg6, result, status))
        assert msg4 == "触发执行数据包回放成功！" and msg5 == "123" and result == "success"
