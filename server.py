#!/usr/bin/env python3
# coding:utf-8

import os
import socket
import time
# 定义全局列表用来存储子文件夹
list1 = []


def deal_file(files,dir_name,dir_socket):
    # 如果打开文件时报错即files为文件夹
    try:
        old_file = open(os.path.join(dir_name.decode(),files),"rb")
    except:
        # 讲导致报错的文件夹放入全局列表等待处理
        global list1
        list1.append(files)
    else:
        #　没有报错则执行读取发送关闭文件
        file_data = old_file.read()
        print("Transporting...")
        dir_socket.send(file_data)

        old_file.close()

def deal_dir():
    # 待完善用于处理子文件夹,需要利用递归完成
    pass


def main():
    print("Start server...")
    print("Waiting client to connect...")
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 固定端口号
    tcp_socket.bind(("",9992))
    # 被动套接字转换为主动套接字
    tcp_socket.listen(128)
    # 将队列中的客户端取出
    dir_socket,client_ip = tcp_socket.accept()
    #　接受客户端消息
    dir_name = dir_socket.recv(1024)
    # 显示文件列表
    file_list = os.listdir(dir_name.decode())
    # 将文件列表发送至客户端
    dir_socket.send(str(file_list).encode())
    # 阻塞0.5s等待发送成功
    time.sleep(0.5)
    # 便利每个文件发送文件内容
    for files in file_list:
        deal_file(files, dir_name, dir_socket)
    global list1
    # 如果全局列表内有文件则
    if list1:
        # 带完善
        pass
    else:
        dir_socket.close()
        print("Finish transport...")
        tcp_socket.close()



if __name__ == '__main__':
    main()
