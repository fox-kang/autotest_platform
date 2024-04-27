from utils.logger import *
from API.Security_Profiles_Api.Association_Analysis_Api.aas import *
from API.System_Management_Api.System_Log_Api.log import *
from common.security_public import *
from common.system_public import *


@allure.feature("关联分析")
class Test_Relevancy:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("安全配置-关联分析-操作-新建-删除")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete_aasrules(self, ID, request, random_string, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            values1 = random_string  # 策略名称
            times = aas().time(cookies)
            tree = '31'  # 规则id
            name = ('data5', 'ruleName')
            treeId = ('data5', 'treeId')
            modifytime1 = ('data5', 'eventMatchBeanList', 0, 'modifytime')
            modifytime2 = ('data5', 'modifytime')
            replace_dict = {
                name: values1,
                modifytime1: times,
                modifytime2: times,
                treeId: tree
            }
            data = a.replace_value_in_yml(aas_file, replace_dict)['data5']
            rsp1 = aas().aasrules_rule(data, cookies)
            ruleId = rsp1.json()['values']['ruleId']
        with allure.step('执行步骤 2'):
            ids = '?ids=' + str(ruleId)
            rsp2 = aas().aasrules_delete(ids, cookies)
            print(rsp2.text)
            msg2 = rsp2.json()['message']
        self.logger.info('开始执行第{}条用例\n新建关联分析策略名称为{}\n删除策略:{}'.format(ID, random_string, msg2))
        assert msg2 == '操作成功'


