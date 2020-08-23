'''
    服务端多进程处理
'''
from multiprocessing import Process
from dict_db import *
import time

class DictServer(Process):
    def __init__(self,connfd):
        self.connfd = connfd
        self.p = Database()
        self.name = ""
        super().__init__()
    def register(self,username,password):

        if self.p.register(username,password):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")


    def logging(self,username,password):
        if self.p.logging(username,password):
            self.connfd.send(b"OK")
            self.name = username
        else:
            self.connfd.send(b"FAIL")

    def find_word(self,word):
        data = self.p.find_word(word,self.name)
        if data:
            self.connfd.send(b"OK")
            time.sleep(0.1)
            self.connfd.send(data.encode())
        else:
            self.connfd.send(b"FAIL")
    def history(self):
        date = self.p.history(self.name)
        for x in date:
            self.connfd.send(str(x).encode())
        time.sleep(0.1)
        self.connfd.send(b"OK")

    def use_remove(self):
        self.p.use_remove(self.name)

    def run(self):
        while 1:
            data = self.connfd.recv(1024).decode()
            data = data.split(" ")
            if data[0] == "Z":
                self.register(data[1],data[2])
            elif data[0] == "A":
                self.logging(data[1],data[2])
            elif data[0] == "C":
                self.find_word(data[1])
            elif data[0] == "H":
                self.history()

            elif data[0] == "E":
                self.use_remove()
                self.connfd.close()
                self.p.cur.close()
                self.p.db.close()
                break