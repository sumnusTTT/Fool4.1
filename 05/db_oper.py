# db_oper.py

# 利用pymysql封装的数据库操作类
# 连接、断开数据库, 执行查询、增删改
import pymysql

from db_conf import *  # 使用配置文件中的四个参数

class DBOper:  # DataBaseOperator 简写  (数据库操作类)
    def __init__(self):  # 构造方法
        # 先创建一个连接对象(因为后续的操作都需要连接对象)
        # None是因为目前还没有指定连接到哪个对象
        self.db_conn = None

    def open_conn(self):  # 连接数据库 
        """为了在类中只建立一次连接"""
        try:
            self.db_conn = pymysql.connect(
                           host, user, passwd, dbname)
        except Exception as e:
            print('数据库连接错误')
            print(e)
        else:  # try语句顺利执行完后会执行
            print('数据库连接成功')

    def close_conn(self):  # 关闭连接
        """在调用连接结束后关闭连接"""
        try:
            self.db_conn.close()  # 关闭连接
        except Exception as e:
            print('数据库连接关闭错误')
            print(e)
        else:  # try语句顺利执行完后会执行
            print('数据库连接关闭成功')

    def do_query(self, sql):  # 查询
        """获取游标, 执行sql语句, 将得到的数据返回"""
        try:
            cursor = self.db_conn.cursor()  # 获取游标
            cursor.execute(sql)  # 执行查询
            result = cursor.fetchall()  # 取出数据
            cursor.close()  # 关闭游标
            return result  # 返回查询结果
        except Exception as e:
            print('执行查询错误')
            print(e)  # 打印异常信息
            return None  # 查询错误, 返回空对象

    def do_update(self, sql):  # 增删改
        """获取游标, 执行sql语句"""
        try:
            cursor = self.db_conn.cursor()  # 获取游标
            result = cursor.execute(sql)  # 执行SQL, 返回值为语句影响了多少笔数据
            self.db_conn.commit()  # 提交事务
            cursor.close()  # 关闭游标
            return result
        except Exception as e:
            self.db_conn.rollback()  # 出错回滚事务
            print("执行SQL出错")
            print(e)
            return None

if __name__ == '__main__':  # 当执行这个py文件(这个文件为主模块)时运行以下语句
    dboper = DBOper()  # 实例化一个数据库操作对象
    dboper.open_conn()  # 打开连接
    # result = dboper.do_query('select * from orders')
    # for r in result:  # 遍历打印结果
    #     print(r)
    sql = '''update orders set amt=amt+100
             where order_id = '201801010001'
    '''
    result = dboper.do_update(sql)  # 将指定订单的金额每次测试增加100
    print('影响笔数:', result)  # result 是上一条修改语句影响到的数据笔数

    dboper.close_conn()  # 关闭连接