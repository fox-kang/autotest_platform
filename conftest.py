import random
import string
import tempfile
import time
import uuid
import yaml
import zipfile
import pytest
from common.login_public import *


@pytest.fixture(autouse=False)
def test_name(request):
    print(request.node.name)


@pytest.fixture(scope='function')
# 清理环境操作
def temp_dir():
    # 创建一个临时目录
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


@pytest.fixture(autouse=False)
def random_mac():
    mac = [random.choice(string.hexdigits.upper()) + random.choice(string.hexdigits.upper()) for _ in range(6)]
    return ':'.join(mac)


@pytest.fixture(autouse=False)
def random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip


@pytest.fixture(autouse=False)
def random_string():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(4))


@pytest.fixture(autouse=False)
def mac_to_yaml(request, random_mac, mac_index):
    """
    :param request: pytest获取用例信息参数
    :param random_mac: 输入随机mac地址
    :param mac_index: 输入mac地址所在文件中的位置
    :return: 返回修改后的mac地址
    """
    count = [0]  # 使用列表使得变量可以在嵌套函数中被修改

    def replace_mac(Data, mac_address, index):
        for key, value in list(Data.items()):
            if isinstance(value, dict):
                replace_mac(value, mac_address, index)
            elif key in ["mac", "src_mac", "dst_mac", "dst", "src"]:
                count[0] += 1
                if count[0] in index:
                    Data[key] = mac_address
                    print("Step: {} 地址为{}".format(key, mac_address))

    file_path = request.node.get_closest_marker("file_path")
    if file_path:
        file_path = file_path.args[0]
        with open(file_path, 'r') as f:
            content = f.read()
        data = yaml.safe_load(content)
        replace_mac(data, random_mac, mac_index)
        with open(file_path, 'w') as f:
            yaml.safe_dump(data, f, allow_unicode=True)
    return random_mac


@pytest.fixture(autouse=False)
def ip_to_yaml(request, random_ip, ip_index):
    """
    :param request: pytest获取用例信息参数
    :param random_ip: 输入随机ip地址
    :param ip_index: 输入ip地址所在文件中的位置
    :return: 返回修改后的ip地址
    """
    count = [0]  # 使用列表使得变量可以在嵌套函数中被修改

    def replace_ip(ipdata, ip_address, index):
        for key, value in list(ipdata.items()):
            if isinstance(value, dict):
                replace_ip(value, ip_address, index)
            # 检查是否匹配到了需要替换的IP的键
            elif key in ["ip", "src_ip", "dst_ip", "dst", "src"]:
                count[0] += 1
                # 当计数符合需要替换的索引时，替换IP并打印对应的键
                if count[0] in index:
                    ipdata[key] = ip_address
                    print("Step: {} 地址为{}".format(key, ip_address))

    file_path = request.node.get_closest_marker("file_path")
    if file_path:
        file_path = file_path.args[0]
        with open(file_path, 'r') as f:
            content = f.read()
        data = yaml.safe_load(content)
        replace_ip(data, random_ip, ip_index)
        with open(file_path, 'w') as f:
            yaml.safe_dump(data, f, allow_unicode=True)
    return random_ip


@pytest.fixture(autouse=True)
def cookies():
    cookie = {'JSESSIONID': 'b07f0c44-aefb-475f-844b-18b00452e5cd'}
    print("Step: cookie为{}".format(cookie))
    return cookie


