#!/usr/bin/env python3
# coding:utf-8

import socket
import os
import threading
import time


def recv_data(files,dir_name,tcp_socket):
    file_data = tcp_socket.recv(1024)
    new_file = open(os.path.join(dir_name+"新", files),"wb")

    new_file.write(file_data)
    new_file.close()
    print("文件%s下载完成" % files)

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(("120.27.238.190", 9992))

    # 向服务器发送要拷贝的文件夹
    dir_name = input("请输入要拷贝的文件夹")
    tcp_socket.send(dir_name.encode())
    # 新建文件夹
    os.mkdir(dir_name+"新")
    # 接受文件列表,循环打开文件写入
    file_list = tcp_socket.recv(1024)
    a = eval(file_list)
    print(a)
    for files in eval(file_list.decode()):
        recv_data(files,dir_name,tcp_socket)


if __name__ == '__main__':
    main()
