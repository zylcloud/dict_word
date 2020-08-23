'''
    客户端第一界面
'''
class Client():
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def client_view01(self):
        print("""
            =======================
            1.注册   2.登录   3.退出
            =======================
                    """)

    def client_view02(self):
        print("""
            ============================
            1.查找单词 2.查看历史记录 3.注销
            ============================
                    """)

    def register(self):
        username = input("请输入你的账号:")
        password = input("请输入你的密码:")
        if " " in username or " " in password:
            print("账号和密码不能出现空格")
            return
        data = "Z" + " " + username + " " + password
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(100).decode()
        if data == "OK":
            print("注册成功")
        else:
            print("账号已存在")

    def log_in(self):
        username = input("请输入账号:")
        password = input("请输入密码:")
        if " " in username or " " in password:
            print("名字和密码不能出现空格")
            return
        data = "A" + " " + username + " " + password
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(100).decode()
        if data == "OK":
            print("登录成功")
            return True
        else:
            print("用户不存在或密码不对")
            return False


    def lookup_word(self):
        word = input("请输入单词:")
        if " " in word:
            print("单词不要出现空格")
            return
        word = "C"+" "+word
        self.sockfd.send(word.encode())

        data = self.sockfd.recv(100)
        if data == b"OK":
            data = self.sockfd.recv(1024*10)
            print(data.decode())
        else:
            print("单词不存在")


    def history(self):
        self.sockfd.send(b"H")
        while True:
            data = self.sockfd.recv(1024)
            if data == b"OK":
                break
            print(data.decode(),end="\n")