from utils.logger import *
from API.Asset_detection_Api.Asset_Topology_Api.topology import *
from common.asset_public import *


@allure.feature("通讯拓扑")
class Test_communicationTopo:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看通讯拓扑图页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_topo(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            rsp1 = topology().topology_getNetworkSegmentTopo(cookies)
            networkSegment = rsp1.json()['result']['networkSegment']
            msg1 = rsp1.json()['message']
            self.logger.info(
                '开始执行第{}条用例,资产名称为{}'.format(ID, networkSegment))
        assert msg1 == "操作成功"
