# order_manage.py

# 订单管理类, 业务逻辑层
from db_oper import *
from order import *

class OrderManage:
    # 初始化方法, 传入 db_oper 是因为要在此类中操作数据库
    def __init__(self, db_oper):
        self.db_oper = db_oper  # 在属性中保存数据操作对象

    # 查询所有订单信息,
    # 返回一个由订单对象构成的列表
    def query_all_order(self):
        order_list = []  # 要返回的订单对象列表
        sql = 'select * from orders'
        result = self.db_oper.do_query(sql)  # 查询
        if not result:  # 查询返回空对象
            print('查询返回空对象')
            return None
        # 查询结果部位空, 取出数据, 创建对象, 并放入列表
        for order_info in result:
            order_id = order_info[0]  # 订单编号
            cust_id = order_info[1]  # 客户编号
            if order_info[5]:  # 订单金额不为空, 转换为浮点数
                amt = float(order_info[5])
            else:  # 金额为空, 默认显示0.00
                amt = 0.00
            order_list.append(
                Order(order_id, cust_id, amt))
        # for 循环结束, 注意缩进!!!
        return order_list  # 返回订单对象列表

if __name__ == '__main__':
    db_oper = DBOper()  # 实例化数据操作对象
    db_oper.open_conn()  # 打开连接

    om = OrderManage(db_oper)  # 实例化订单管理对象
    db_oper.close_conn()  # 关闭连接
    for o in order_list:
        print(o)
    order_list = om.query_all_order()  # 查询所有订单