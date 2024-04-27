from API.System_Management_Api.Engine_Management_Api.engine import engine
from common.system_public import engine_file
from utils.logger import *
from API.Security_Profiles_Api.Exception_Management_Api.exclude import *
from common.security_public import *


@allure.feature('例外管理')
class TestException:
    @pytest.mark.smoke('这是一条冒烟用例')
    @pytest.mark.file_path(exclude_file)
    @pytest.mark.parametrize('ID, ip_index', [('001', [1, 2])])
    @allure.story("新建例外管理")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_exception(self, request, ID, ip_to_yaml, ip_index, cookies):
        self.logger = get_log(request.node.name)
        with allure.step("执行步骤: 1"):
            data = a.read_yml_file(exclude_file)['data4']
            rsp1 = exclude().policies_exclude_add(data, cookies)
            msg = rsp1.json()['message']
            msg1 = rsp1.json()['values']['excludePlicyId']
        with allure.step("执行步骤: 2"):
            data = a.read_yml_file(exclude_file)['data2']
            rsp2 = exclude().policies_exclude_list(data, cookies)
            msg2 = rsp2.json()['values']['policiesBeans'][0]['id']
        with allure.step("执行步骤: 3"):
            data = a.read_yml_file(exclude_file)['data2']
            rsp3 = exclude().policies_exclude_list(data, cookies)
            id = rsp3.json()['values']['policiesBeans'][0]['id']
        with allure.step("执行步骤: 4"):
            values = id
            policyIdStr = ('data6', 'policyIdStr')
            replace_dict = {
                policyIdStr: values
            }
            data = a.replace_value_in_yml(exclude_file, replace_dict)['data6']
            rsp4 = exclude().policies_exclude_delete(data, cookies)
            msg4 = rsp4.json()['message']
        with allure.step("执行步骤: 5"):
            rsp5, status5 = exclude().policies_exclude_taskstatus_(cookies)
        with allure.step("执行步骤 6"):
            data = a.read_yml_file(engine_file)['data10']
            rsp6, status6 = engine().devices_taskstatus_(data, cookies)
            time.sleep(10)
        self.logger.info(
            '开始执行第{}条用例,创建例外管理ip地址为{},接口返回信息为{},{},{},{},例外id为{}'
            .format(ID, ip_to_yaml, msg, msg4, status5, status6, msg1))
        assert msg1 == msg2

