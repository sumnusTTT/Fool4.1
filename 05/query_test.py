# 用来示例用pymysql模块来查询数据库中的数据

# 1. 导入pymysql模块
import pymysql

from db_conf import *
# 2. 创建数据库连接
conn = pymysql.connect(host, user,
       passwd, dbname)  # 连接到eshop库, 并将库(连接对象)绑定到conn上

# 3. 创建游标对象
cursor = conn.cursor()  # cursor 游标(用来执行SQL语句)

# 4. 使用游标对象提供的方法, 执行SQL语句
sql = 'select * from orders'
cursor.execute(sql)  # 执行语句
result = cursor.fetchall()  # 将cursor中的数据都提取出来

# 5. 提交事务(如果需要) - 对select语句来说不需要, 改为打印数据
for r in result:  # result 返回的是元组, 所以进行遍历
    order_id = r[0]  # 订单编号
    cust_id = r[1]  # 客户编号
    if not r[5]:
        amt = 0.00
    else:
        amt = float(r[5])  # 订单金额
    print('订单编号:%s, 客户编号:%s, 金额:%.2f' % (order_id, cust_id, amt))

# 6. 关闭游标
cursor.close()
# 7. 关闭数据库连接对象
conn.close()