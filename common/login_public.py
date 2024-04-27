import binascii
import os
import time
import rsa
import pytest
import ddddocr
import hashlib
import requests
import urllib3
import allure
from utils.lib_config import *

# 关闭警告
urllib3.disable_warnings()

a = configuration()
config = a.joint_path(os.path.dirname(__file__), '../config.yml')


# 封装获取验证码的函数
class Public:
    def __init__(self):
        self.ip = ""
        self.authorize = ""
        self.handle_str()
        self.login_str()

    # 封装获取验证码以及验证码cookie方法
    def get_code(self):
        url = self.ip + a.read_yml_file(config)["code"]
        res = requests.get(url=url, verify=False)
        cookies = self.get_code_cookie(res)
        code_path = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['ceshi.jpg'])
        with open(code_path, mode="wb") as f:
            f.write(res.content)
        ocr = ddddocr.DdddOcr(show_ad=False)
        with open(code_path, 'rb') as files:
            r = files.read()
        ui = ocr.classification(r)
        print("登录验证码为{}".format(ui))
        return ui, cookies

    @staticmethod
    def get_code_cookie(res):
        cookies = res.cookies
        cookies.set('lang', 'zh-CN', domain=a.read_yml_file(config)["host"])
        cookie_pairs = []
        for cookie in cookies:
            # 提取键和值
            key = cookie.name
            value = cookie.value
            # 将键值对添加到 cookie_pairs 列表中
            cookie_pairs.append(f"{key}={value}")
        # 使用 ";" 将 cookie_pairs 中的键值对合并为一个字符串
        cookie_pairs.reverse()
        merged_cookie = "; ".join(cookie_pairs)
        # print(merged_cookie)
        return merged_cookie

    # 封装sha1加密函数
    @staticmethod
    def sha1(input_string):
        sha1 = hashlib.sha1()
        sha1.update(input_string.encode('utf-8'))
        return sha1.hexdigest()

    # 生成pem格式公钥
    def pubkey(self, Cookie):
        url = self.ip + a.read_yml_file(config)["rsa-key"]
        head = {'Cookie': Cookie}
        r = requests.get(url=url,  headers=head, verify=False)

        data = r.json()
        exponent = data["values"]['exponent']
        exponents = int(exponent, 16)
        modules = data["values"]['modulus']
        modulus = int(modules, 16)
        public_key = rsa.PublicKey(modulus, exponents)
        return public_key

    def password(self, Cookie):
        public_key = self.pubkey(Cookie)
        message = self.sha1(a.read_yml_file(config)["passwd"]).encode('utf-8')  # 输入明文密码
        crypto = rsa.encrypt(message, public_key)
        # 输出加密后的密码
        passwd = binascii.hexlify(crypto).decode('utf-8')
        print('登录密码为{}'.format(passwd))
        return passwd

    # 获取cookie
    def cookie(self):
        url = self.authorize
        staticVCode, Cookie = Public().get_code()
        data = {"username": a.read_yml_file(config)["username"],
                "password": self.password(Cookie),
                "staticVCode": staticVCode,
                "scales": 'on'}
        head = {"Cookie": Cookie}
        r = requests.post(url=url, data=data, headers=head, verify=False)
        return dict(r.cookies)

    def handle_str(self):
        self.ip = (a.read_yml_file(config)["scheme"]
                   + a.read_yml_file(config)["host"]
                   + a.read_yml_file(config)["port"])
        return self.ip

    def login_str(self):
        self.authorize = (self.ip
                          + a.read_yml_file(config)["login_url"]
                          + a.read_yml_file(config)["client_id"]
                          + a.read_yml_file(config)["response_type"]
                          + a.read_yml_file(config)["redirect_uri"])
        # print(self.authorize)
        return self.authorize


if __name__ == '__main__':
    P = Public()
    P.cookie()
