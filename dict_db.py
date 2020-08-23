'''
    服务端连接数据库代码
'''
import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port = 3306,
                                  user = "root",
                                  password = "123456",
                                  database = "dict",
                                  charset = "utf8")
        self.cur = self.db.cursor()
    def register(self,username,password):
        sql = "select username from user where username = %s;"
        self.cur.execute(sql,[username])
        if self.cur.fetchone():
            return False
        else:
            sql = "insert into user(username,password) values(%s,%s);"
            self.cur.execute(sql,[username,password])
            self.db.commit()
            return True

    def logging(self,username,password):
        sql = "select username,password from user where username = %s"
        self.cur.execute(sql,[username])
        data = self.cur.fetchone()
        if data:
            if data[-1] == password:
                return True
            else:
                return False
        else:
            return False

    def find_word(self,word,usename):
        sql = "insert into use_history(name,word) values(%s,%s)"
        self.cur.execute(sql,[usename,word])

        sql = "select mean from words where word = %s"
        self.cur.execute(sql,[word])
        data = self.cur.fetchone()
        if data:
            print(data)
            return data[0]
        else:
            return False
    def history(self,username):
        sql = "select * from use_history where name = %s order by id desc limit 10;"
        self.cur.execute(sql,[username])
        data = self.cur.fetchall()
        print(data)
        return data

    def use_remove(self,use_name):
        sql = "delete from use_history where name = %s;"
        self.cur.execute(sql,[use_name])





