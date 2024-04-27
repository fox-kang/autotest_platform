from utils.logger import *
from API.Flow_Analysis_Api.Key_Behavior_Api.kbi import *
from common.flow_public import *
from Download.down_pcap import *


@allure.feature("关键行为")
class TestKeyevents:

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("关键事件-取证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_keyevents_obtain(self, request, ID, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            endtime = kbi().time(cookies)
            starttime = str(int(endtime) - 86400000)
            endTime = ('data1', 'endTime')
            startTime = ('data1', 'startTime')
            replace_dict = {
                endTime: endtime,
                startTime: starttime
            }
            data = a.replace_value_in_yml(kbi_file, replace_dict)['data1']
            rsp1 = kbi().alerts_(data, cookies)
            datagram = rsp1.json()['values']['result'][0]['generic']['datagram']
            dst_ip = rsp1.json()['values']['result'][0]['generic']['dst_ip']
            dst_mac = rsp1.json()['values']['result'][0]['generic']['dst_mac']
            src_ip = rsp1.json()['values']['result'][0]['generic']['src_ip']
            src_mac = rsp1.json()['values']['result'][0]['generic']['src_mac']
        with allure.step("执行步骤: 2"):
            times = kbi().time(cookies)
            Datagram = ('data2', 'datagram')
            dstIp = ('data2', 'dstIp')
            dstMac = ('data2', 'dstMac')
            srcIp = ('data2', 'srcIp')
            srcMac = ('data2', 'srcMac')
            time_stamp = ('data2', 'timestamp')
            replace_dict = {
                time_stamp: times,
                Datagram: datagram,
                dstIp: dst_ip,
                dstMac: dst_mac,
                srcIp: src_ip,
                srcMac: src_mac
            }
            data = a.replace_value_in_yml(kbi_file, replace_dict)['data2']
            files = kbi().alerts_download_pcap(data, cookies)
            down_pcap(files, '../../Download')
