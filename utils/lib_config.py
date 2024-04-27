# 加载配置信息
import yaml
import os
import zipfile
import time


class configuration:
    # 封装读取yml文件函数
    @staticmethod
    def read_yml_file(file_path):
        """
        :param file_path: 输入文件地址
        :return: 返回文件数据
        """
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def open_pcap_file(zip_file_path, file_name):
        """
        :param zip_file_path: 输入zip文件路径
        :param file_name: 输入文件名称
        :return: 返回文件
        """
        # 打开 Zip 文件
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            # 获取 Zip 文件中所有的文件列表
            file_list = zip_file.namelist()

            if file_name in file_list:
                # 提取ZIP文件中的指定文件
                zip_file.extract(file_name)
                # 对目标URL执行文件上传
                with open(file_name, 'rb') as file_to_upload:
                    file_data = file_to_upload.read()
                files = {'file': (os.path.basename(file_name), file_data)}
                # 删除临时文件
                os.remove(file_name)
                return files
            else:
                print("文件不存在")

    @staticmethod
    def update_yml_value(data, keys, value):
        """
        :param data: 输入要更新的数据文件
        :param keys: 输入要更新的内容所在的键
        :param value: 输入要更新内容的值
        """
        if len(keys) == 1:
            data[keys[0]] = value
        else:
            key = keys[0]
            if isinstance(key, int):
                if key >= len(data):
                    raise IndexError(f"Index {key} is out of range")
                configuration().update_yml_value(data[key], keys[1:], value)
            elif key not in data:
                raise KeyError(f"Key '{key}' not found in YAML")
            else:
                configuration().update_yml_value(data[key], keys[1:], value)

    def replace_value_in_yml(self, yaml_file, replacement_dict):
        """
        :param yaml_file: 输入yml文件名称
        :param replacement_dict: 输入要替换的字典
        :return: 返回替换后的数据
        """
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        for keys, value in replacement_dict.items():
            self.update_yml_value(data, keys, value)
        return data

    @staticmethod
    def status_test(max_attempts, interval, status_rsp, status_result):
        """
        :param max_attempts: 输入最大次数
        :param interval: 输入间隔时间
        :param status_rsp: 输入响应数据
        :param status_result: 输入响应结果
        :return: 返回响应数据，结果
        """
        for _ in range(max_attempts):
            rsp = status_rsp
            status = status_result
            if status in ["success", "ok"]:
                result = status
                print("回放状态在预定时间内变为{}".format(result))
                break
            else:
                time.sleep(interval)
        else:
            raise Exception("回放状态没有在预定时间内变为'成功'")
        return rsp, result

    # 转换路径方法为绝对路径
    @staticmethod
    def translate_path(base_path, data_path):
        """
        :param base_path: 输入项目文件路径
        :param data_path: 输入数据文件路径
        :return: 返回数据文件的绝对路径
        """
        file = os.path.abspath(os.path.join(os.path.join(os.fspath(base_path), os.fspath(data_path.lstrip('\\')))))
        return file

    # 拼接路径
    @staticmethod
    def joint_path(base_path, sub_path):
        """

        :param base_path: 输入项目文件路径
        :param sub_path: 输入数据文件路径
        :return: 拼接文件路径
        """
        absolute = os.path.join(base_path, sub_path)
        return absolute
