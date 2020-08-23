'''
    客户端入口代码
'''
from socket import *
from client01 import *
import sys

class dict_client:
    def __init__(self):
        self.sock()
        self.client = Client(self.sockfd)
    def sock(self):
        self.sockfd = socket()
        self.sockfd.connect(("0.0.0.0",8899))

    def client_view01(self):
        while True:
            self.client.client_view02()
            try:
                cmd = input("命令:")
            except:
                print("欢迎下次使用")
                self.sockfd.send("E".encode())
                self.sockfd.close()
                sys.exit("欢迎下次使用")
            if cmd == "1":
                self.client.lookup_word()
            elif cmd == "2":
                self.client.history()

            elif cmd == "3":
                break
            else:
                print("请输入正确的选项")


    def start(self):
        while True:
            self.client.client_view01()
            try:
                data = input("命令:")
            except:
                print("欢迎下次使用")
                self.sockfd.send("E".encode())
                self.sockfd.close()
                break
            if data == "1":
                self.client.register()

            elif data == "2":
                if self.client.log_in():
                    self.client_view01()

            elif data == "3":
                data = "E"
                self.sockfd.send(data.encode())
                self.sockfd.close()
                break
            else:
                print("输入正确的选项")

def entry_code():
    p = dict_client()
    p.start()

if __name__ == '__main__':
    entry_code()