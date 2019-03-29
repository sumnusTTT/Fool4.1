# db_oper.py
# 利用pymysql封装的数据库操作类
# 连接，断开数据库，执行查询，增删改
from db_conf import *
import pymysql
class DBOper:   #数据库操作类

    def __init__(self): #构造方法
        self.db_conn = None  #连接对象

    def open_conn(self):      #连接数据库
        try:
            self.db_conn = pymysql.connect(
                host,user,passwd,dbname)
        except Exception as e:
            print("数据库连接错误")
            print(e)
        else:
            print("数据库连接成功")

    def close_conn(self):       #关闭连接
        try:
            self.db_conn.close()   #关闭
        except Exception as e:
            print("数据库连接关闭错误")
            print(e)
        else:
            print("数据库连接关闭成功")

    def do_query(self,sql):     #查询
        try:
            cursor = self.db_conn.cursor() #获取游标
            cursor.execute(sql)  #先执行查询
            result = cursor.fetchall()  #获取数据
            cursor.close()  #关闭游标
            return result   #返回查询结果
        except Exception as e:
            print("执行查询错误")
            print(e)    #打印异常信息
            return None   #查询错误，返回空对象

    # def do_update(self,sql):#增删改

if __name__ == '__main__':
    dboper = DBOper()   #实例一个数据操作对象
    dboper.open_conn()  #打开连接
    result = dboper.do_query("select * from orders")
    for r in result:    #遍历打印结果
        print(r)
    
    dboper.close_conn() #关闭连接

