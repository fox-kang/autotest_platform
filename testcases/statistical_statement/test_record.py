from utils.logger import *
from API.Statistical_statement_Api.Report_Template_Api.template import *
from common.statistical_public import *


@allure.feature("统计报表")
class Test_statistical:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看报表记录页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_template(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(report_file)['data1']
            rsp = template().accessory_list(data, cookies)
            name = [item['accessoryName'] for item in rsp.json()['result']['list']]
            self.logger.info('开始执行第{}条用例,报表文件名称有{}'.format(ID, name))
            assert rsp.json()['message'] == '操作成功'
