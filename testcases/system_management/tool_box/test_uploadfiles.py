from utils.logger import *
from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import *
from common.baseline_public import *
from common.system_public import *


@allure.feature("数据包回放")
class Test_upload:

    @pytest.mark.slow("这是条测试时间较长的用例")
    @pytest.mark.flaky(reruns=1, reruns_delay=40)
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('001',
                                  a.read_yml_file(data_packet_file)['modulus_pcap']),
                             ]
                             )
    @allure.story("上传数据包并回放查看状态")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_upload_file(self, ID, request, pcap_data, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            rsp1 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp2, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg2 = rsp2.json()["message"]
        self.logger.info(
            '开始执行第{}条用例,参数为{},接口返回信息为{},回放状态在预定时间内变为{}'
            .format(ID, pcap_data, rsp2.text, result))
        assert msg1 == "操作成功" and msg2 == "触发执行数据包回放成功！" and result == "success"
