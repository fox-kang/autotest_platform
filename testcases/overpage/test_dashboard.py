from utils.logger import *
from API.Overview_Page_Api.dashboards import *


@allure.feature("总览页面")
class Test_dashboard:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看总览页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_dashboard(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            rsp = dashboards().dashboards_twentyFourHours(cookies)
            result = rsp.json()['result']
            self.logger.info('开始执行第{}条用例,接口返回信息为{}'.format(ID, result))
        assert rsp.json()['message'] == '操作成功'
