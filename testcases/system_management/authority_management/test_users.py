from utils.logger import *
from API.System_Management_Api.Authority_Management_Api.user import *
from API.System_Management_Api.Authority_Management_Api.role import *
from common.system_public import *


@allure.feature("权限管理")
class Test_users:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看用户管理页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_users(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(users_file)['data1']
            rsp = User().users(data, cookies)
            name = [(item['id'], item['name']) for item in rsp.json()['values']['roleEntityList']]
            self.logger.info('开始执行第{}条用例,所属角色有{}'.format(ID, name))
            assert rsp.json()['message'] == '操作成功'

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['002'])
    @allure.story("查看角色管理页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_role(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(role_file)['data1']
            rsp = role().roles(data, cookies)
            name = [item['name'] for item in rsp.json()['values']['pageBean']['list']]
            self.logger.info('开始执行第{}条用例,所属角色有{}'.format(ID, name))
            assert rsp.json()['message'] == '操作成功'
