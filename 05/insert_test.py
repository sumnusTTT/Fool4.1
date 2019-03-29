# 用来示例用pymysql模块来向数据库中插入数据

# 1. 导入pymysql模块
import pymysql

from db_conf import *
try:
    # 2. 创建数据库连接
    conn = pymysql.connect(host, user,
        passwd, dbname)  # 连接到eshop库, 并将库(连接对象)绑定到conn上
    # 3. 创建游标对象
    cursor = conn.cursor()  # cursor 游标(用来执行SQL语句)
    # 4. 使用游标对象提供的方法, 执行SQL语句
    # sql = '''insert into orders(order_id, cust_id, amt)
    # values('201801010001','C0001',234.56)
    # '''
    # sql = '''delete from orders where cust_id='C0001'
    # '''
    sql = '''update orders set amt=2000.00 where cust_id='C0001'
    '''
    cursor.execute(sql)  # 执行语句

    # 5. 提交事务(如果需要)
    conn.commit()  # 提交事务 - 对 insert 语句而言, 默认开启了一个事务, 在Python中需要执行提交事务
    # print('插入成功')
    # print('删除成功')
    # print('修改成功')

except Exception as e:
    conn.rollback()  # 如果报错, 需要先回滚事务
    print(e)

# 6. 关闭游标
cursor.close()
# 7. 关闭数据库连接对象
conn.close()