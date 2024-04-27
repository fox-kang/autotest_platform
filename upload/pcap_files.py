import shutil
import zipfile
import os

# 要上传的 PCAP 文件所在的文件夹路径
PCAP_DIR = 'C:/Users/Administrator/Desktop/pcap/pcap_files/入侵'

# 封装后的文件名
ZIP_NAME = "入侵.zip"


def zip_pcap_files(pcap_dir, zip_name):
    """

    :param pcap_dir: 要上传的 PCAP 文件所在的文件夹路径
    :param zip_name: 封装后的文件名
    :return: 生成zip文件夹
    """
    # 创建临时文件夹用于存放待上传的PCAP文件
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 复制PCAP文件到临时文件夹
    pcap_files = os.listdir(pcap_dir)
    for file in pcap_files:
        shutil.copy2(os.path.join(pcap_dir, file), temp_dir)

    # 压缩临时文件夹中的PCAP文件
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk(temp_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_dir))
    zipf.close()

    # 删除临时文件夹
    shutil.rmtree(temp_dir)


# 调用封装函数
zip_pcap_files(PCAP_DIR, ZIP_NAME)
