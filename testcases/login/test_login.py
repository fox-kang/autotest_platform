from utils.logger import *
from API.Login_Api.authorize import *


@allure.feature("登录功能")
class Test_login:

    @allure.story("有效用户名和密码")
    @allure.testcase(Public().login_str())  # 链接到具体的测试用例地址
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    @pytest.mark.parametrize('ID', ['001'])
    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.xfail(reason="已知问题，待修复")
    def test_login(self, request, ID):
        self.logger = get_log(request.node.name)
        r = Login().login()
        self.logger.info('开始执行第{}条用例，接口返回信息为{}'.format(ID, r))
        assert r.status_code == 200
