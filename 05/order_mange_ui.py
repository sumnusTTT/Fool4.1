# order_manage_ui.py

# 订单管理用户接口层(视图层)
# 只负责用户发出命令、显示执行结果

from db_oper import *
from order import *
from order_mange import *
# 全局变量, 提前创建避免每个函数中都要再次创建
db_oper = None  # 数据操作对象
om = None       # OrderManage对象

# 开始程序主体, 打印订单
menu = '''
----------- 订单管理程序 -----------
  1. 查询所有订单
  2. 根据订单号查询
  3. 新增订单
'''
print(menu)  # 打印菜单

db_oper = DBOper()  # 创建数据库操作对象
db_oper.open_conn()  # 打开连接
om = OrderManage(db_oper)  # 创建订单管理对象

oper = input('请选择要执行的操作: ')
if oper == '1':  # 查询所有订单
    order_list = om.query_all_order()
    for a in order_list:
        print(a)
elif oper == '2':  # 根据订单号查询
    pass  # 还没定义
elif oper == '3':  # 新增订单
    pass  # 还没定义
db_oper.close_conn()  # 关闭连接