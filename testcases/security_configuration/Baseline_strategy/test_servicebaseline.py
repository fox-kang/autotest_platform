import allure
from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.link import *
from common.baseline_public import *


@allure.feature("服务基线")
class TestNewLinkBaseline:  # 服务基线

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.file_path(link_file)
    @pytest.mark.parametrize('ID,ip_index', [('018', [1])])
    @allure.id('015')
    @allure.story("新建服务基线并应用")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_link(self, request, ID, cookies, ip_to_yaml, ip_index):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(link_file)['data1']
            rsp1 = link().baseline_link(data, cookies)
            msg1 = rsp1.json()["message"]
        with allure.step("执行步骤 2"):
            data = a.read_yml_file(link_file)['data5']
            rsp2 = link().baseline_link_disable(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            data = a.read_yml_file(link_file)['data4']
            rsp3 = link().baseline_link_enable(data, cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            data = a.read_yml_file(link_file)['data6']
            rsp4 = link().baseline_link_updateConfig(data, cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤 5"):
            rsp5, status = link().baseline_link_taskstatus(cookies)
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(link_file)['data2']
            rsp6 = link().baseline_link_filter(data, cookies)
            msg6 = rsp6.json()["message"]
        with allure.step("执行步骤 7"):
            data = a.read_yml_file(link_file)['data7']
            rsp7 = link().baselineConfigLog_status(data, cookies)
            msg7 = rsp7.json()["message"]
        self.logger.info('用例执行完毕，接口返回信息为{}'.format(rsp5.text))
        assert (msg1 == "操作成功"
                and msg2 == "操作成功，还需应用下发才可生效！"
                and msg3 == "操作成功，还需应用下发才可生效！"
                and msg4 == "服务基线批量事件设置成功"
                and status == "ok"
                and msg6 == "操作成功"
                and msg7 == "操作成功"
                )

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['019'])
    @allure.story("删除服务基线并应用")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete_link(self, request, ID, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(link_file)['data2']
            rsp1 = link().baseline_link_filter(data, cookies)
            msg1 = rsp1.json()["values"]['pageBean']['list'][0]['id']
        with allure.step("执行步骤 2"):
            id = ('data3', 'ids')
            replacement_dict = {
                id: [msg1]
            }
            data = a.replace_value_in_yml(link_file, replacement_dict)['data3']
            rsp2 = link().baseline_link_delete(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            rsp3, status = link().baseline_link_taskstatus(cookies)
        self.logger.info('用例{}执行完毕，接口返回信息为{},{},基线应用状态为{}'.format(ID, msg1, msg2, status))
        assert (msg2 == '操作成功' and status == 'ok')
