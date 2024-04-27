import allure

from common.system_public import log_file
from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.business import *
from API.System_Management_Api.System_Log_Api.log import *
from common.baseline_public import *


@allure.feature("业务基线")
class TestNewBusinessBaseline:  # 业务基线

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.file_path(business_file)
    @pytest.mark.parametrize('ID, ip_index', [('001', [1])])
    @allure.story("新建业务基线")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_business(self, request, ID, cookies, ip_to_yaml, ip_index):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            rsp1 = business().protocols_all(cookies)
            msg1 = rsp1.json()["message"]
        with allure.step('执行步骤 2'):
            data = a.read_yml_file(business_file)['data1']
            rsp2 = business().protocols(data, cookies)
            msg2 = rsp2.json()['message']
        with allure.step('执行步骤 3'):
            data = a.read_yml_file(business_file)['data2']
            rsp3 = business().baseline_business_add(data, cookies)
            msg3 = rsp3.json()['message']
        with allure.step("执行步骤 4"):
            rsp4, status = business().baseline_business_taskstatus(cookies)
            msg4 = rsp4.json()["message"]
        self.logger.info('用例{}执行完毕,接口返回信息为{},{},{},{}'.format(ID, msg1, msg2, msg3, msg4))
        assert (msg1 == "操作成功"
                and msg2 == "操作成功"
                and msg3 == "操作成功"
                and status == 'ok')

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.file_path(business_file)
    @pytest.mark.parametrize('ID, ip_index', [('002', [3])])
    @allure.story("编辑业务基线")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_update_business(self, request, ID, cookies, ip_to_yaml, ip_index):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(business_file)['data6']
            rsp1 = business().baseline_business_page(data, cookies)
        with allure.step('执行步骤 2'):
            values1 = rsp1.json()['result']['list'][0]['id']
            values2 = rsp1.json()['result']['list'][0]['pid']
            values3 = rsp1.json()['result']['list'][0]['rid']
            id = ('data5', 'id')
            rid = ('data5', 'rid')
            pid = ('data5', 'pid')
            replacement_dict = {
                id: values1,
                rid: values2,
                pid: values3
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data5']
            rsp2 = business().baseline_business_update(data, cookies)
            msg2 = rsp2.json()['message']
        with allure.step("执行步骤 3"):
            rsp3, status = business().baseline_business_taskstatus(cookies)
            msg3 = rsp3.json()["message"]
        self.logger.info('用例{}执行完毕,接口返回信息为{},{},基线应用状态为{}'.format(ID, msg2, msg3, status))
        assert (msg2 == "操作成功"
                and msg3 == "操作成功"
                and status == 'ok')

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID', ['003'])
    @allure.story("删除业务基线并应用")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete_link(self, request, ID, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(business_file)['data6']
            rsp1 = business().baseline_business_page(data, cookies)
            msg1 = rsp1.json()["result"]['list'][0]['id']
        with allure.step("执行步骤 2"):
            id = ('data3', 'ids')
            replacement_dict = {
                id: [msg1]
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data3']
            rsp2 = business().baseline_business_delete(data, cookies)
            msg2 = rsp2.json()["message"]
        with allure.step("执行步骤 3"):
            rsp3, status = business().baseline_business_taskstatus(cookies)
        self.logger.info('用例{}执行完毕，接口返回信息为{},{},基线应用状态为{}'.format(ID, msg1, msg2, status))
        assert (msg2 == '删除业务基线成功' and status == 'ok')

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, ip_index', [('004', [1])])
    @allure.story("业务基线-应用按钮功能验证")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_apply_button(self, request, ID, cookies, ip_to_yaml, ip_index, random_ip):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤 1"):
            data = a.read_yml_file(business_file)['data6']
            rsp1 = business().baseline_business_page(data, cookies)
            msg1 = [item['id'] for item in rsp1.json()['result']['list']]
        with allure.step("执行步骤 2"):
            ids = msg1
            IDS = ('data3', 'ids')
            replacement_dict = {
                IDS: ids
            }
            data = a.replace_value_in_yml(asset_file, replacement_dict)['data3']
            rsp2 = business().baseline_business_delete(data, cookies)
            msg2 = rsp2.json()['message']
        with allure.step("执行步骤 3"):
            rsp3, status3 = business().baseline_business_taskstatus(cookies)
            msg3 = rsp3.json()["message"]
        with allure.step("执行步骤 4"):
            rsp4, status4 = business().baseline_business_taskstatus(cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤 5"):
            endtime = str(int(time.time()) * 1000)
            starttime = str(int(endtime) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStrats = ('data1', 'timeStrats')
            replacement_dict = {
                timeEnds: endtime,
                timeStrats: starttime
            }
            data = a.replace_value_in_yml(log_file, replacement_dict)['data1']
            rsp5 = log().pg_logs_operationLogList(data, cookies)
            msg5 = rsp5.json()['result']['logs'][0]['message']
        with allure.step('执行步骤 6'):
            rsp6 = business().protocols_all(cookies)
            msg6 = rsp6.json()["message"]
        with allure.step('执行步骤 7'):
            data = a.read_yml_file(business_file)['data1']
            rsp7 = business().protocols(data, cookies)
            msg7 = rsp7.json()['message']
        with allure.step('执行步骤 8'):
            data = a.read_yml_file(business_file)['data2']
            rsp8 = business().baseline_business_add(data, cookies)
            msg8 = rsp8.json()['message']
        with allure.step('执行步骤 9'):
            data = a.read_yml_file(business_file)['data6']
            rsp9 = business().baseline_business_page(data, cookies)
            msg9 = rsp9.json()['result']['list'][0]['status']
        with allure.step("执行步骤 10"):
            rsp10, status10 = business().baseline_business_taskstatus(cookies)
            msg10 = rsp10.json()["message"]
        with allure.step('执行步骤 11'):
            data = a.read_yml_file(business_file)['data6']
            rsp11 = business().baseline_business_page(data, cookies)
            msg11 = rsp11.json()['result']['list'][0]['status']
        with allure.step('执行步骤 12'):
            values1 = rsp11.json()['result']['list'][0]['id']
            values2 = rsp11.json()['result']['list'][0]['pid']
            values3 = rsp11.json()['result']['list'][0]['rid']
            src = random_ip
            id = ('data5', 'id')
            rid = ('data5', 'rid')
            pid = ('data5', 'pid')
            SRC = ('data5', 'src')
            replacement_dict = {
                id: values1,
                rid: values2,
                pid: values3,
                SRC: src
            }
            data = a.replace_value_in_yml(business_file, replacement_dict)['data5']
            rsp12 = business().baseline_business_update(data, cookies)
            msg12 = rsp12.json()['message']
        with allure.step('执行步骤 13'):
            data = a.read_yml_file(business_file)['data6']
            rsp13 = business().baseline_business_page(data, cookies)
            msg13 = rsp13.json()['result']['list'][0]['status']
        with allure.step("执行步骤 14"):
            rsp14, status14 = business().baseline_business_taskstatus(cookies)
            msg14 = rsp14.json()["message"]
        with allure.step('执行步骤 15'):
            data = a.read_yml_file(business_file)['data6']
            rsp15 = business().baseline_business_page(data, cookies)
            msg15 = rsp15.json()['result']['list'][0]['status']
        with allure.step("执行步骤 16"):
            rsp16, status16 = business().baseline_business_taskstatus(cookies)
            msg16 = rsp16.json()["message"]
        with allure.step('执行步骤 17'):
            data = a.read_yml_file(business_file)['data6']
            rsp17 = business().baseline_business_page(data, cookies)
            msg17 = rsp17.json()['result']['list'][0]['status']
        self.logger.info('用例第{}条执行完毕，接口返回信息为{}\n基线应用状态为:{},{},{},{},{}\n新建基线后查看基线状态为:{}\n应用基线后查看基线状态为:{}\n'
                         '系统日志记录为:{}\n编辑基线后查看基线状态为:{}\n再次应用基线后查看基线状态为:{}\n多次应用基线后查看基线状态为:{}'
                         .format(ID, msg2, status3, status4, status10, status14, status16, msg9, msg11, msg5, msg13,
                                 msg15, msg17))
        assert (msg3 == "操作成功"
                and msg4 == "操作成功"
                and msg6 == "操作成功"
                and msg7 == "操作成功"
                and msg8 == "操作成功"
                and msg10 == "操作成功"
                and msg12 == "操作成功"
                and msg14 == "操作成功"
                and msg16 == "操作成功")
