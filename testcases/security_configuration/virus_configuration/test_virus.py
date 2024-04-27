import time

from utils.logger import *
from API.Security_Profiles_Api.Virus_Configuration_Api.virus import *
from API.System_Management_Api.Engine_Management_Api.engine import *
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from API.System_Management_Api.Tool_Box_Api.ping import *
from API.Threat_Detection_Api.Virus_Detection_Api.virus import *
from common.security_public import *
from common.system_public import *
from common.threat_public import *


@allure.feature("病毒检测")
class TestVirus:  # 病毒检测
    @pytest.mark.slow("这是条测试时间较长的用例")
    @pytest.mark.flaky(reruns=1, reruns_delay=40)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['virus_pcap']),
                             ]
                             )
    @allure.story("病毒配置功能验证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_virus(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(Virus_file)['data3']
            rsp1 = antivirus().antivirus_template_update(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            data = a.read_yml_file(engine_file)['data4']
            rsp2 = engine().devices_update(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            data = a.read_yml_file(engine_file)['data10']
            rsp3, status = engine().devices_taskstatus_(data, cookies)
            time.sleep(30)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(engine_file)['data1']
            rsp7 = engine().devices_pagination(data, cookies)
            msg7 = rsp7.json()["message"]
        with allure.step("执行步骤 5"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤 7"):
            values1 = virus().time(cookies)  # 获取访问页面时的时间戳
            values2 = str(int(values1)-86400000)
            timeEnds = ('data1', 'timeEnds')
            startTime = ('data1', 'timeStarts')
            replacement_dict = {
                timeEnds: values1,
                startTime: values2
            }
            data = a.replace_value_in_yml(Virus_file, replacement_dict)['data1']
            rsp6 = virus().virusWarning_list(data, cookies)
            msg6 = rsp6.json()["message"]
        self.logger.info(
            '开始执行第{}条用例,参数为{},页面时间戳为{},接口返回信息为{},{},{},{},{},{},{},回放状态在预定时间内变为{},引擎应用状态为{}'
            .format(ID, pcap_data, values1, msg1, msg2, msg3, msg4, msg5, msg6, msg7, result, status))
        assert msg5 == "触发执行数据包回放成功！" and result == "success" and status == "ok"

    @pytest.mark.smoke('这是一条冒烟用例')
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("新建病毒配置")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_virus(self, ID, request, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            values = random_string
            name = ('data2', 'templateName')
            replacement_dict = {
                name: values
            }
            data1 = a.replace_value_in_yml(Virus_file, replacement_dict)['data2']
            rsp1 = antivirus().antivirus_template_add(data1, cookies)
            msg1 = rsp1.json()['message']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(Virus_file)['data1']
            rsp2 = antivirus().antivirus_template_get(data, cookies)
            msg2 = rsp2.json()['result'][0]['templateName']
            id = rsp2.json()['result'][0]['id']
        with allure.step("执行步骤: 3"):
            values1 = id
            ID = ('data4', 'ids')
            replacement_dict = {ID: values1}
            data = a.replace_value_in_yml(Virus_file, replacement_dict)['data4']
            rsp3 = antivirus().antivirus_template_delete(data, cookies)
            msg3 = rsp3.json()['message']
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(engine_file)['data10']
            rsp4, status = engine().devices_taskstatus_(data, cookies)
            time.sleep(10)
            msg4 = rsp4.json()["message"]
        self.logger.info(
            '开始执行第{}条用例,参数为{},创建策略名称为{},接口返回信息为{},{}'.format(ID, data1, values, msg1, msg2))
        assert msg2 == values and msg3 == '操作成功' and msg4 == '操作成功'

    @pytest.mark.slow("这是条测试时间较长的用例")
    @pytest.mark.flaky(reruns=1, reruns_delay=40)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('003',
                                  a.read_yml_file(data_packet_file)['virus_pcap']),
                             ]
                             )
    @allure.story("安全配置-病毒检测-新建模板-文件白名单是否生效")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_virus_file_whitelist(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            rsp1 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp2, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            values1 = virus().time(cookies)  # 获取访问页面时的时间戳
            values2 = str(int(values1)-86400000)
            timeEnds = ('data1', 'timeEnds')
            startTime = ('data1', 'timeStarts')
            replacement_dict = {
                timeEnds: values1,
                startTime: values2
            }
            data = a.replace_value_in_yml(Virus_file, replacement_dict)['data1']
            rsp3 = virus().virusWarning_list(data, cookies)
            fileName1 = [item['fileName'] for item in rsp3.json()['result']]
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(Virus_file)['data1']
            rsp4 = antivirus().antivirus_template_get(data, cookies)
            msg4 = rsp4.json()['result'][0]['templateName']
            id = rsp4.json()['result'][0]['id']
        with allure.step("执行步骤 5"):
            values3 = 'aWNlLTIuYW1y'  # ice-2.amr
            values4 = id
            whiteList = ('data3', 'whiteList')
            IDS = ('data3', 'id')
            replacement_dict = {
                IDS: values4,
                whiteList: values3
            }
            data = a.replace_value_in_yml(Virus_file, replacement_dict)['data3']
            rsp5 = antivirus().antivirus_template_update(data, cookies)
            msg5 = rsp5.json()['message']
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(engine_file)['data10']
            rsp6, status = engine().devices_taskstatus_(data, cookies)
            time.sleep(30)
            msg6 = rsp6.json()["message"]
        with allure.step("执行步骤 7"):
            rsp7 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg7 = rsp7.json()["message"]
        with allure.step("执行步骤 8"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp8, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg8 = rsp8.json()["message"]
        with allure.step("执行步骤 9"):
            values1 = virus().time(cookies)  # 获取访问页面时的时间戳
            values2 = str(int(values1)-86400000)
            timeEnds = ('data1', 'timeEnds')
            startTime = ('data1', 'timeStarts')
            replacement_dict = {
                timeEnds: values1,
                startTime: values2
            }
            data = a.replace_value_in_yml(Virus_file, replacement_dict)['data1']
            rsp9 = virus().virusWarning_list(data, cookies)
            fileName2 = [item['fileName'] for item in rsp9.json()['result']]
        self.logger.info(
            '开始执行第{}条用例\n接口返回信息为{},{},{},{},{},{},{}\n检测出的病毒文件有{}\n{}\n'
            .format(ID, msg1, msg2, msg4, msg5, msg6, msg7, msg8, fileName1, fileName2))


