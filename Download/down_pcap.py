import os


def down_pcap(response, save_folder):
    """
    :param response:  响应数据
    :param save_folder: 保存路径
    :return:
    """
    if response.status_code == 200:
        # 获取文件名
        content_disposition = response.headers.get("Content-Disposition")  # 自定义保存的文件名
        file = content_disposition.split("filename=")[1]
        file_name = file.strip('"')
        # 构建完整的保存路径
        save_path = os.path.join(save_folder, file_name)

        # 将响应数据写入文件
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("PCAP 文件保存成功！")
    else:
        print("PCAP 文件下载失败：", response.status_code)
