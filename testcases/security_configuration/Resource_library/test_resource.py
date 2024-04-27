import random
import time

from API.System_Management_Api.Tool_Box_Api.Data_packet_replay import Data_packet
from common.system_public import data_packet_file
from utils.logger import *
from API.Security_Profiles_Api.Resource_Library_Api.resource import *
from API.Security_Profiles_Api.Resource_Library_Api.operator import *
from API.Security_Profiles_Api.Resource_Library_Api.baselinegenerators import *
from API.Security_Profiles_Api.Resource_Library_Api.chart import *
from API.Security_Profiles_Api.Resource_Library_Api.organization import *
from API.Security_Profiles_Api.Resource_Library_Api.vulnCves import *
from API.Security_Profiles_Api.Resource_Library_Api.risk import *
from API.Security_Profiles_Api.Resource_Library_Api.virus import *
from API.Security_Profiles_Api.Resource_Library_Api.weakPass import *
from API.Security_Profiles_Api.Weak_Password_Configuration_Api.weakpass import *
from API.Vulnerability_Api.Weak_Password_Api.weak import *
from API.System_Management_Api.System_Log_Api.log import *
from common.security_public import *
from common.vulnerability_public import *
from common.system_public import *


@allure.feature("资源库")
class Test_management:
    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['001'])
    @allure.story("查看资源库页面")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_view_resource(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            numbers = random.choice(['2', '4'])
            for i in numbers:
                datasource = ('data2', 'dataSource')
                replacement_dict = {
                    datasource: i
                }
            data = a.replace_value_in_yml(resource_file, replacement_dict)['data2']
            rsp1 = resource().templates_page(data, cookies)
            name1 = [item['name'] for item in rsp1.json()['result']['list']]
        with allure.step('执行步骤 2'):
            data = a.read_yml_file(operator_file)['data1']
            rsp2 = operator().protocols(data, cookies)
            name2 = [item['name'] for item in rsp2.json()['result']]
        with allure.step('执行步骤 3'):
            data = a.read_yml_file(baselinegenerators_file)['data1']
            rsp3 = baselinegenerators().baselinegenerators_page(data, cookies)
            name3 = [item['generator_Name'] for item in rsp3.json()['values']['pageBean']['list']]
        with allure.step('执行步骤 4'):
            data = a.read_yml_file(chart_file)['data1']
            rsp4 = chart().chart_list(data, cookies)
            name4 = [item['chartName'] for item in rsp4.json()['result']['list']]
        with allure.step('执行步骤 5'):
            data = a.read_yml_file(organization_file)['data1']
            rsp5 = organization().organization_list(data, cookies)
            name5 = [item['organization_name'] for item in rsp5.json()['values']['unitList']['list']]
        with allure.step('执行步骤 6'):
            data = a.read_yml_file(vulnCves_file)['data2']
            path = a.read_yml_file(vulnCves_file)['CveList']
            rsp6 = vulnCves().vulnCves_select(data, path, cookies)
            name6 = [item['vulnname'] for item in rsp6.json()['result']['cveVos']]
        with allure.step('执行步骤 7'):
            data = a.read_yml_file(risk_file)['data1']
            path = a.read_yml_file(risk_file)['page']
            rsp7 = risk().high_risk_port(data, path, cookies)
            name7 = [item['application'] for item in rsp7.json()['result']['list']]
        with allure.step('执行步骤 8'):
            data = a.read_yml_file(Virus_file)['data1']
            list_path = a.read_yml_file(virus_file)['list']
            page_path = a.read_yml_file(virus_file)['page']
            rsp8 = Virus().virus_library_virus(None, list_path, cookies)
            rsp9 = Virus().virus_library_virus(data, page_path, cookies)
            name8 = [item['name'] for item in rsp8.json()['result']]
            name9 = rsp9.json()['result']['list']
        with allure.step('执行步骤 9'):
            data = a.read_yml_file(weakPass_file)['data1']
            rsp10 = weakPass().weakPasswordStore_page(data, cookies)
            name10 = [item['vendorName'] for item in rsp10.json()['result']['list']]
        self.logger.info(
            '开始执行第{}条用例,资产名称有{}\n协议名称有{},\n业务基线生成器名称有{},\n图标名称有{},\n'
            '组织单元类型有{},\n漏洞名称有{},\n危险端口库常用服务有{},\n病毒名称有{},\n弱口令影响产品名称有{}'
            .format(ID, name1, name2, name3, name4, name5, name6, name7, name8, name9, name10))

    @pytest.mark.slow('这是一条标记时间比较长的测试')
    @pytest.mark.parametrize('ID, pcap_data',
                             [
                                 ('002',
                                  a.read_yml_file(data_packet_file)['123456_pcap']),
                             ]
                             )
    @allure.story("安全配置-资源库-弱口令库-新建弱口令规则-使能功能")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_weak_rule(self, ID, request, cookies, pcap_data):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            password = '123456'
            name = 'test'
            pwd = ('data3', 'pwd')
            user = ('data3', 'user')
            replace_dict = {
                pwd: password,
                user: name
            }
            data = a.replace_value_in_yml(weakPass_file, replace_dict)['data3']
            rsp1 = weakPass().weakPasswordStore_add(data, cookies)
            msg1 = rsp1.json()['message']
        with allure.step('执行步骤 2'):
            rsp2, status = weak().weakPass_taskstatus_(cookies)
        with allure.step('执行步骤 3'):
            data = a.read_yml_file(weak_password_file)['data1']
            rsp3 = weak().baselineConfigLog_percent(data, cookies)
            msg3 = rsp3.json()['message']
        with allure.step("执行步骤: 4"):
            rsp4 = Data_packet().toolbox_import_package(pcap_data['zip_file_path'], pcap_data['file_name'], cookies)
            msg4 = rsp4.json()["message"]
        with allure.step("执行步骤: 5"):
            data = a.read_yml_file(data_packet_file)['data1']
            rsp5, result = Data_packet().toolbox_perform_replay(data, cookies)
            msg5 = rsp5.json()["message"]
        with allure.step("执行步骤: 6"):
            end = weakness().time(cookies)
            start = str(int(end) - 300000)
            endTime = ('data2', 'endTime')
            startTime = ('data2', 'startTime')
            replace_dict = {
                startTime: start,
                endTime: end
            }
            data = a.replace_value_in_yml(weak_file, replace_dict)['data2']
            rsp6 = weakness().weakPass_list(data, cookies)
            weakUsername = rsp6.json()['values']['list'][0]['weakUsername']
            weakPassword = rsp6.json()['values']['list'][0]['weakPassword']
        with allure.step("执行步骤: 7"):
            data = a.read_yml_file(weakPass_file)['data1']
            rsp7 = weakPass().weakPasswordStore_page(data, cookies)
            id = rsp7.json()['result']['list'][0]['id']
        with allure.step("执行步骤: 8"):
            values = id
            ids = ('data5', 'ids')
            replace_dict = {
                ids: [values]
            }
            data = a.replace_value_in_yml(weakPass_file, replace_dict)['data5']
            rsp8 = weakPass().weakPasswordStore_delete(data, cookies)
            msg8 = rsp8.json()['message']
        with allure.step('执行步骤 9'):
            rsp9, status2 = weak().weakPass_taskstatus_(cookies)
        self.logger.info(
            '开始执行第{}条用例,新建弱口令库{}\n弱口令应用状态{},{}\n弱口令配置{}\n数据包回放状态为{}\n弱口令账户为{}\n弱口令密码为{}'
            .format(ID, msg1, status, status2, msg3, result, weakUsername, weakPassword))
        assert (msg4 == '操作成功'
                and msg5 == '触发执行数据包回放成功！'
                and msg8 == '删除弱口令成功'
                and weakUsername == 'test'
                and weakPassword == '123456')

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['003'])
    @allure.story("【资源库-危险端口库】批量删除 ")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_delete_risk(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(risk_file)['data2']
            path = a.read_yml_file(risk_file)['path2']
            rsp1 = risk().high_risk_port(data, path, cookies)
            msg1 = rsp1.json()['message']
        with allure.step('执行步骤 2'):
            data = a.read_yml_file(risk_file)['data1']
            path = a.read_yml_file(risk_file)['page']
            rsp2 = risk().high_risk_port(data, path, cookies)
            id = rsp2.json()['result']['list'][0]['id']
        with allure.step('执行步骤 3'):
            ids = ('data4', 'ids')
            replace_dict = {
                ids: [id]
            }
            data = a.replace_value_in_yml(risk_file, replace_dict)['data4']
            path = a.read_yml_file(risk_file)['path4']
            rsp3 = risk().high_risk_port(data, path, cookies)
            msg3 = rsp3.json()['message']
            time.sleep(5)
        with allure.step('执行步骤 4'):
            end = log().time(cookies)
            start = str(int(end) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStarts = ('data1', 'timeStarts')
            replace_dict = {
                timeEnds: end,
                timeStarts: start
            }
            data = a.replace_value_in_yml(log_file, replace_dict)['data1']
            rsp4 = log().pg_logs_operationLogList(data, cookies)
            msg4 = rsp4.json()['result']['logs'][0]['message']
        with allure.step('执行步骤 5'):
            id1 = '1'
            ids = ('data4', 'ids')
            replace_dict = {
                ids: [id1]
            }
            data = a.replace_value_in_yml(risk_file, replace_dict)['data4']
            path = a.read_yml_file(risk_file)['path4']
            rsp5 = risk().high_risk_port(data, path, cookies)
            msg5 = rsp5.json()['message']
            time.sleep(5)
        with allure.step('执行步骤 6'):
            end = log().time(cookies)
            start = str(int(end) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStarts = ('data1', 'timeStarts')
            replace_dict = {
                timeEnds: end,
                timeStarts: start
            }
            data = a.replace_value_in_yml(log_file, replace_dict)['data1']
            rsp6 = log().pg_logs_operationLogList(data, cookies)
            msg6 = rsp6.json()['result']['logs'][0]['message']
        self.logger.info(
            '开始执行第{}条用例,新增自定义危险端口库:{}\n尝试删除自定义危险端口库:{}\n系统日志记录:{}\n尝试删除系统内置危险端口库:{}\n系统日志记录:{}'
            .format(ID, msg1, msg3, msg4, msg5, msg6))
        assert msg3 == '删除自定义端口成功' and msg5 == '删除系统预置端口失败'

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['004'])
    @allure.story("【资源库-危险端口库】筛选-危险级别")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_risk_level(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            level_list = ["low", "medium", "high", "critical"]
            level = random.choice(level_list)
            print(level)
            severity = ('data1', 'severity')
            replace_dict = {
                severity: [level]
            }
            data = a.replace_value_in_yml(risk_file, replace_dict)['data1']
            path = a.read_yml_file(risk_file)['page']
            rsp1 = risk().high_risk_port(data, path, cookies)
            msg1 = [item['severity'] for item in rsp1.json()['result']['list']]
            # 将列表转换为集合，获取唯一元素
            unique_values = set(msg1)
            # 如果集合的长度为1，则列表中的所有值相同
            if len(unique_values) == 1:
                value = unique_values.pop()
                print("筛选危险等级为:", value)
            else:
                print("列表中的值不全相同")
        self.logger.info('开始执行第{}条用例, 筛选危险级别为{}'.format(ID, value))
        assert level == value

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['005'])
    @allure.story("【资源库-危险端口库】筛选-来源")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_risk_dataSource(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            level_list = ["1", "2"]
            level = random.choice(level_list)
            print(level)
            dataSource = ('data1', 'dataSource')
            replace_dict = {
                dataSource: level
            }
            data = a.replace_value_in_yml(risk_file, replace_dict)['data1']
            path = a.read_yml_file(risk_file)['page']
            rsp1 = risk().high_risk_port(data, path, cookies)
            msg1 = [item['dataSource'] for item in rsp1.json()['result']['list']]
            # 将列表转换为集合，获取唯一元素
            unique_values = set(msg1)
            if len(unique_values) == 0:
                print("该来源没有相关数据")
            # 如果集合的长度为1，则列表中的所有值相同
            elif len(unique_values) == 1:
                value = unique_values.pop()
                print("筛选危险等级为:", value)
            else:
                print("列表中的值不全相同")
        self.logger.info('开始执行第{}条用例, 筛选来源为:{}\n(其中1为系统预置2为自定义)'.format(ID, level))

    @pytest.mark.smoke('这是条冒烟用例')
    @pytest.mark.parametrize('ID', ['006'])
    @allure.story("图表-复制图表-复制弹框-确定-删除-确定")
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    def test_chart_copy_bounce(self, ID, request, cookies):
        self.logger = get_log(request.node.name)
        with allure.step('执行步骤 1'):
            data = a.read_yml_file(chart_file)['data1']
            rsp1 = chart().chart_list(data, cookies)
            id1 = rsp1.json()['result']['list'][0]['id']
        with allure.step('执行步骤 2'):
            data = str(id1)
            rsp2 = chart().chart_copy_(data, cookies)
            msg2 = rsp2.json()['message']
        with allure.step('执行步骤 3'):
            endtime = log().time(cookies)
            starttime = str(int(endtime) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStarts = ('data1', 'timeStarts')
            replace_dict = {
                timeEnds: endtime,
                timeStarts: starttime
            }
            data = a.replace_value_in_yml(log_file, replace_dict)['data1']
            rsp3 = log().pg_logs_operationLogList(data, cookies)
            msg3 = rsp3.json()['result']['logs'][0]['message']
        with allure.step('执行步骤 4'):
            data = a.read_yml_file(chart_file)['data1']
            rsp4 = chart().chart_list(data, cookies)
            id4 = rsp4.json()['result']['list'][0]['id']
        with allure.step('执行步骤 5'):
            groupIds = ('data8', 'groupIds')
            replace_dict = {
                groupIds: [id4]
            }
            data = a.replace_value_in_yml(chart_file, replace_dict)['data8']
            rsp5 = chart().chart_delete(data, cookies)
            msg5 = rsp5.json()['message']
        with allure.step('执行步骤 6'):
            endtime = log().time(cookies)
            starttime = str(int(endtime) - 1800000)
            timeEnds = ('data1', 'timeEnds')
            timeStarts = ('data1', 'timeStarts')
            replace_dict = {
                timeEnds: endtime,
                timeStarts: starttime
            }
            data = a.replace_value_in_yml(log_file, replace_dict)['data1']
            rsp6 = log().pg_logs_operationLogList(data, cookies)
            msg6 = rsp6.json()['result']['logs'][0]['message']
        self.logger.info('开始执行第{}条用例\n{}\n日志记录为{}\n{}\n日志记录为{}'.format(ID, msg2, msg3, msg5, msg6))
        assert msg2 == '图表复制成功' and msg5 == '删除成功'
