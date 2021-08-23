# import os, sys
#
# file_list = os.listdir(os.getcwd())
#
# for item in file_list:
#     if '.log' in item:
#         os.remove(item)
#
#         print(item)
#
# file_list = os.listdir(os.getcwd())
# print(file_list)


# import paramiko
#
# ssh = paramiko.SSHClient()  # 创建SSH对象
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
# ssh.connect(hostname='120.26.106.222', port=22, username='root', password='Zycj@2020688')  # 连接服务器
#
# stdin, stdout, stderr = ssh.exec_command(r'cd /mnt/mysql_dump;rm *')  # 执行命令并获取命令结果
# # stdin为输入的命令
# # stdout为命令返回的结果
# # stderr为命令错误时返回的结果
# res, err = stdout.read(), stderr.read()
# result = res if res else err
# print(result.decode('utf8'))
# ssh.close()  # 关闭连接