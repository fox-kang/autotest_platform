from utils.logger import *
from API.Security_Profiles_Api.Baseline_Strategy_Api.protocol import *
from common.baseline_public import *


@allure.feature("协议基线")
class TestNewProtocolBaseline:  # 协议基线
    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('011', a.read_yml_file(protocol_file)['data1'])])
    @allure.story("新建协议基线")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_getAllProtocols(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_getAllProtocols(data, cookies)
        self.logger.info('开始执行第{}条用例,参数为{},接口返回信息为{}'.format(ID, data, rsp))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('012', a.read_yml_file(protocol_file)['data2']['protocolId'])])
    @allure.story("选择新增的协议基线并确定")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_add_or_update(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_add(cookies)
        self.logger.info('开始执行第{}条用例,协议编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('013', a.read_yml_file(protocol_file)['data3'])])
    @allure.story("删除协议基线并确定")
    @allure.severity(allure.severity_level.NORMAL)  # 优先级
    def test_delete(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_delete(cookies)
        self.logger.info('开始执行第{}条用例,协议编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('014', a.read_yml_file(protocol_file)['data4'])])
    @allure.story("协议基线列表")
    @allure.severity(allure.severity_level.NORMAL)  # 优先级
    def test_list(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_list(cookies)
        self.logger.info('开始执行第{}条用例,协议编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('015', a.read_yml_file(protocol_file)['data5'])])
    @allure.story("应用协议基线")
    @allure.severity(allure.severity_level.NORMAL)  # 优先级
    def test_configuration(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_configuration(cookies)
        self.logger.info('开始执行第{}条用例,编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('016', a.read_yml_file(protocol_file)['data6'])])
    @allure.story("协议基线状态")
    @allure.severity(allure.severity_level.NORMAL)  # 优先级
    def test_status(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baselineConfigLog_status(cookies)
        self.logger.info('开始执行第{}条用例,编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功"

    @pytest.mark.smoke("这是条冒烟用例")
    @pytest.mark.parametrize('ID, data', [('017', a.read_yml_file(protocol_file)['data7'])])
    @allure.story("修改协议基线状态")
    @allure.severity(allure.severity_level.NORMAL)  # 优先级
    def test_change_status(self, request, ID, data, cookies):
        self.logger = get_log(request.node.name)
        rsp = protocol().baseline_protocol_change(cookies)
        self.logger.info('开始执行第{}条用例,编号为{},接口返回信息为{}'.format(ID, data, rsp.text))
        assert rsp.json()["message"] == "操作成功，还需应用下发才可生效！"
