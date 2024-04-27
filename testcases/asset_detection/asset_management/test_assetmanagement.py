from utils.logger import *
from API.Asset_detection_Api.Asset_Management_Api.management import *
from common.asset_public import *


@allure.feature("资产管理")
class Test_management:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看资产列表")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_asset(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            data = a.read_yml_file(asset_management_file)['data3']
            rsp1 = management().asset_(data, cookies)
            msg1 = rsp1.json()["message"]
            name = rsp1.json()['result'][0]['name']
        self.logger.info(
            '开始执行第{}条用例,资产名称为{}'.format(ID, name))
        assert msg1 == "操作成功"

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("新建资产-编辑资产-删除资产")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_update_asset(self, ID, request, cookies, random_string):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):

            data = a.read_yml_file(asset_management_file)['data7']
            rsp1 = management().asset_add(data, cookies)
            result = rsp1.json()['result']
        with allure.step("执行步骤: 2"):
            values = random_string
            id = ('data5', 'id')
            name = ('data5', 'name')
            replace_dict = {
                id: result,
                name: values
            }
            data = a.replace_value_in_yml(asset_management_file, replace_dict)['data5']
            rsp2 = management().asset_update(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤: 3"):
            ids = ('data6', 'ids')
            replace_dict = {
                ids: [result]
            }
            data = a.replace_value_in_yml(asset_management_file, replace_dict)['data6']
            rsp3 = management().asset_delete(data, cookies)
            msg3 = rsp3.json()['message']
        self.logger.info(
            '开始执行第{}条用例,接口返回信息为{}'.format(ID, result, msg3))
        assert msg2 == "操作成功"

