import random
import string

from common.baseline_public import *
from common.login_public import *

data = a.read_yml_file(asset_file)


class random_str:
    @staticmethod
    def generate_random_mac():
        mac = [random.choice(string.hexdigits.upper()) + random.choice(string.hexdigits.upper()) for _ in range(6)]
        return ':'.join(mac)

    # 生成一个随机 MAC 地址
    random_mac = generate_random_mac()
    data['data1']["mac"] = random_mac
    # 将更新后的字典写入原始 YAML 文件
    with open(asset_file, 'w') as f:
        yaml.safe_dump(data, f)

    @staticmethod
    # 生成随机IP地址
    def generate_random_ip():
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return ip

    # 生成随机IP地址
    random_ip = generate_random_ip()
    # 将生成的IP地址添加到YAML数据中
    data['data1']["ip"] = random_ip
    # 将更新后的字典写入原始 YAML 文件
    with open(asset_file, 'w') as f:
        yaml.safe_dump(data, f)


#
if __name__ == '__main__':
    R = random_str()
    R.generate_random_mac()
