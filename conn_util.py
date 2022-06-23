import json


def send_data(sock, login_type, data_args):
    '''发送报文长度和报文主体'''
    data_dict = dict()
    data_dict["login"] = login_type
    data_dict["args"] = data_args
    data_dict = json.dumps(data_dict)
    data_dict = data_dict.encode()
    data_len = '{:<15}'.format(len(data_dict))  # 报头长度
    print(data_len)
    sock.send(data_len.encode())  # 发送报头长度
    sock.send(data_dict)  # 发送报文主体


def receive_data_len(sock):
    '''接收响应报文长度'''
    rcv_data_len = sock.recv(15).decode()
    rcv_data_len = int(rcv_data_len.strip())
    return rcv_data_len


def receive_main_data(data_len, sock):
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
