import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 现在可以导入 common 模块
from common.login_public import *
# 忽略https证书验证
urllib3.disable_warnings()

if __name__ == '__main__':
    # testcase = input('请输入用例路径:'.format())
    pytest.main(['../testcases', '--alluredir=../reports/allure', '--clean-alluredir'])
    # os.system(f"allure generate .{allure} -o {html} --clean")
