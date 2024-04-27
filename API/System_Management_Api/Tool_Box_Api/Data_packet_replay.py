import inspect
import time

from API.Api_action import *
from common.login_public import *


class Data_packet:

    def __init__(self):
        self.method = Api_method()

    @allure.step("上传数据包")
    def toolbox_import_package(self, zip_path, filename, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        files = a.open_pcap_file(zip_path, filename)
        rsp = self.method.http_post_data(url, None, None, files, cookie)
        return rsp

    def toolbox_replay_status(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("回放数据包并查看状态")
    def toolbox_perform_replay(self, data, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/api/' + url_route
        rsp = self.method.http_post_json(url, data, None, None, cookie)
        max_attempts = 20  # 最大检查次数为20次
        interval = 3  # 每隔3秒检查一次
        for _ in range(max_attempts):
            status_rsp = Data_packet().toolbox_replay_status(cookie)
            status_result = status_rsp.json()["result"]["result"]

            if status_result == "success":
                result = status_result
                print("回放状态在预定时间内变为{}".format(result))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("回放状态没有在预定时间内变为'成功'")
        return rsp, result
