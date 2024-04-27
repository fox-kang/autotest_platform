import paramiko


class SSH:
    @staticmethod
    def ssh(hostname, port, username, password, command):
        """
        :param hostname: 输入主机ip地址
        :param port: 输入主机端口号
        :param username: 输入用户名
        :param password: 输入密码
        :param command: 输入命令(多个命令用;隔开)
        :return: 返回打印数据
        """

        # 创建client客户端对象
        client = paramiko.SSHClient()
        # 自动添加远程主机的密钥（不进行验证）
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        # 执行命令
        stdin, stdout, stderr = client.exec_command(command)
        # 打印命令输出结果
        output = stdout.read().decode('utf-8')
        client.close()
        return output


if __name__ == '__main__':
    SSH().ssh('10.0.8.6', '10022', 'rayleigh', 'Silvers$R7',
              'sudo tcpreplay -i veth-taa-0 -x 100 -l 1 /home/data_package/modbus_tcp_02.pcap')
