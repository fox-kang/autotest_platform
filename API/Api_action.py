from common.login_public import *


class Api_method:

    @staticmethod
    def http_get(url, headers, data, cookies=True):
        """
        :param url: # 地址
        :param headers: # 请求头
        :param data: # 请求参数
        :param cookies: # 请求cookie
        :return: #  返回相应数据
        """
        return requests.get(url=url, headers=headers, params=data, cookies=cookies, verify=False)

    @staticmethod
    def http_post_data(url, data, headers, files, cookies=True):
        """
        :param url:
        :param data:
        :param headers:
        :param cookies:
        :param files:
        :return:
        """
        return requests.post(url=url, data=data, headers=headers, cookies=cookies, files=files, verify=False)

    @staticmethod
    def http_post_json(url, data, headers, files, cookies=True):
        """
        :param url:
        :param data:
        :param headers:
        :param cookies:
        :param files:
        :return:
        """
        return requests.post(url=url, json=data, headers=headers, cookies=cookies, files=files, verify=False)

    @staticmethod
    def http_delete(url, data, headers, cookies=True):
        """
        :param url:
        :param data:
        :param headers:
        :param cookies:
        :return:
        """
        return requests.post(url=url, data=data, headers=headers, cookies=cookies, verify=False)

    @staticmethod
    def http_put(url, data, headers, cookies=True):
        """
        :param url:
        :param data:
        :param headers:
        :param cookies:
        :return:
        """
        return requests.post(url=url, data=data, headers=headers, cookies=cookies, verify=False)