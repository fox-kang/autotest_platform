import allure

from API.Security_Profiles_Api.Baseline_Strategy_Api.autogenerate import autogenerate
from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.asset import *
from API.Asset_detection_Api.Asset_Discovery_Api.discovery import *
from API.Asset_detection_Api.Asset_Management_Api.management import *
from common.baseline_public import *
from common.asset_public import *


@allure.feature("资产基线")
class TestNewAssetBaseline:  # 资产基线

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.file_path(asset_file)
    @pytest.mark.parametrize('ID, mac_index, ip_index', [('001', [1], [1])])
    @allure.story("新建-应用资产基线-转正式资产-删除资产-自学习")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add(self, request, ID, mac_to_yaml, ip_to_yaml, cookies, mac_index, ip_index):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(asset_file)['data1']
            rsp1 = asset().baseline_asset_add(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            data = a.read_yml_file(asset_file)['data5']
            rsp2 = asset().asset_baseline_configuration_(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            data = a.read_yml_file(asset_file)['data2']
            rsp3 = asset().baseline_asset_list(data, cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(asset_discovery_file)['data3']
            rsp4 = discovery().asset_(data, cookies)
            msg4 = rsp4.json()['result'][0]['id']
        with allure.step("执行步骤 5"):
            ids = ('data4', 'ids')
            replacement_dict = {
                ids: [msg4]
            }
            data = a.replace_value_in_yml(asset_discovery_file, replacement_dict)['data4']
            rsp5 = discovery().asset_correction(data, cookies)
            msg5 = rsp5.json()['message']
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(asset_management_file)['data3']
            rsp6 = management().asset_(data, cookies)
            msg6 = rsp6.json()['result'][0]['id']
        with allure.step("执行步骤 7"):
            ids = ('data8', 'ids')
            replacement_dict = {
                ids: [msg6]
            }
            data = a.replace_value_in_yml(asset_management_file, replacement_dict)['data8']
            rsp7 = management().asset_delete(data, cookies)
            msg7 = rsp7.json()['message']
        with allure.step("执行步骤 8"):
            rsp8 = autogenerate().time(cookies)
            endtime = rsp8.json()['values']['currentTime']
        with allure.step("执行步骤 9"):
            endTime = endtime
            startTime = str(int(endTime)-1800000)
            end = ('data2', 'common', 'endTime')
            start = ('data2', 'common', 'startTime')
            replacement_dict = {
                end: endTime,
                start: startTime
            }
            data = a.replace_value_in_yml(autogenerate_file, replacement_dict)['data2']
            rsp9 = autogenerate().baseline_autogenerate_start(data, cookies)
            msg9 = rsp9.json()['message']
        with allure.step("执行步骤 10"):
            rsp10, status10 = autogenerate().baseline_autogenerate_status(cookies)
        with allure.step("执行步骤 11"):
            data = a.read_yml_file(autogenerate_file)['data1']
            rsp11 = autogenerate().baseline_autogenerate_log(data, cookies)
            msg11 = rsp11.json()['result']['list'][0]['result']
        self.logger.info(
            '用例执行完毕,接口返回信息为{},资产数据id为{},mac地址为{},ip为{}\n学习状态为{}\n最新历史自学习结果为{}'
            .format(msg1, msg4, mac_to_yaml, ip_to_yaml, status10, msg11))
        assert (msg1 == "操作成功"
                and msg2 == "操作成功"
                and msg3 == "操作成功"
                and msg5 == "操作成功"
                and msg7 == "操作成功"
                and msg9 == "操作成功"
                and msg4 == msg6)

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("删除资产基线")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete(self, request, ID, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            source = '1'
            datasource = ('data2', 'dataSource')
            replacement_dict = {
                datasource: source
            }
            data = a.replace_value_in_yml(asset_file, replacement_dict)['data2']
            rsp1 = asset().baseline_asset_list(data, cookies)
            msg1 = [item['id'] for item in rsp1.json()['result']]
        with allure.step("执行步骤 2"):
            ids = msg1
            IDS = ('data3', 'ids')
            replacement_dict = {
                IDS: ids
            }
            data = a.replace_value_in_yml(asset_file, replacement_dict)['data3']
            rsp2 = asset().baseline_asset_delete(data, cookies)
            msg2 = rsp2.json()['message']
        with allure.step("执行步骤 3"):
            data = a.read_yml_file(asset_file)['data5']
            rsp3 = asset().asset_baseline_configuration_(data, cookies)
            msg3 = rsp3.json()["message"]
        self.logger.info('用例执行完毕，自学习资产列表id为{}'.format(msg1))
        assert msg2 == "操作成功" and msg3 == "操作成功"

