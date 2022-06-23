import socket
import json
import threading
import random
# import smtp_mail
# import server_mysql
import os.path
import hashlib

from conn_util import *

id = ["18991384379"]
dict_global = dict()

def login_register(conn):
    try:
        while True:
            received_len = conn.recv(15).decode()
            if len(received_len) == 0:
                break
            received_len = int(received_len.strip())
            data_rec = receive_data(received_len, conn)
            data_rec = json.loads(data_rec)
            if data_rec["login"] == 0:  # 退出请求
                break
            elif data_rec["login"] == 1:  # 手机验证码登录
                veri_login_dict = dict()
                if data_rec["args"]["phone_number"] in id:
                    if dict_global[data_rec["args"]["phone_number"]] == \
                            data_rec["args"]["verify_code"]:
                        veri_login_dict["return"] = 1
                else:
                    veri_login_dict["return"] = 2
                send_data(conn, 1, veri_login_dict)
            elif data_rec["login"] == 2:  # 手机/账号密码登录
                pass
            elif data_rec["login"] == 3:  # 注册
                pass
            elif data_rec["login"] == 4:  # 修改密码
                pass
            elif data_rec["login"] == 5:  # 重置密码
                pass
            elif data_rec["login"] == 6:  # 发送验证短消息
                rand_code = random_six()
                dict_global[data_rec["args"]["phone_number"]] = rand_code
                data_dict = dict()
                data_dict["phone_number"] = data_rec["args"]["phone_number"]
                data_dict["random_code"] = rand_code
                send_data(conn, 6, data_dict)
                print(str(data_rec))
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print('端口1连接关闭')


def receive_data(data_len, sock):
    '''接收报文正文'''
    size = 0
    tmp = b''
    while size < data_len:
        data = sock.recv(data_len - size)
        if not data:
            break
        tmp += data
        size += len(data)
    tmp = tmp.decode()
    return tmp


def send_phone_msg(phone_num, random_num):
    pass


def random_six():
    tmp_str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        tmp_str += ch
    return tmp_str


if __name__ == "__main__":
    sock_login = socket.socket()  # 用于响应验证码发送、登录、注册等请求功能
    sock_login.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_login.bind(("127.0.0.1", 9999))
    sock_login.listen(5)

    conn, address = sock_login.accept()
    print(address, "login 端口已连接")
    threading.Thread(target=login_register, args=(conn,)).start()
