'''
    在线字典服务端入口代码
'''
from socket import *
from signal import *
from dict_01_class import DictServer


signal(SIGCHLD,SIG_IGN)


def entry_code():
    sockfd = socket()
    sockfd.bind(("0.0.0.0",8899))
    sockfd.listen(5)
    while True:
        connfd,addr = sockfd.accept()
        print(addr,"连接服务器")
        p = DictServer(connfd)
        p.start()
if __name__ == '__main__':
    entry_code()
