#!/usr/bin/python
# -*- coding:utf-8 -*
import sys
sys.path.append('/usr/local/lib/python2.7')

import datetime
import unittest
from fs_test import MyTestSuite
import fs_util
import fs_test
start_time = datetime.datetime.now()

# 构造测试集
suite = unittest.TestSuite()
suite.addTest(MyTestSuite("test_stations"))   # 查询站点
suite.addTest(MyTestSuite("test_edge"))   # 查询路网
suite.addTest(MyTestSuite("test_completion"))   # 通过关键字查询
suite.addTest(MyTestSuite("test_login"))   # 登陆
suite.addTest(MyTestSuite("test_user_info"))   # 个人信息
suite.addTest(MyTestSuite("test_balance"))   # 获取余额
suite.addTest(MyTestSuite("test_update_passwd"))   # 更新密码
suite.addTest(MyTestSuite("test_estimation"))   # 获取预估路线
suite.addTest(MyTestSuite("test_order"))   # 创建订单
suite.addTest(MyTestSuite("test_payment"))   # 支付订单
suite.addTest(MyTestSuite("test_detail"))   # 订单详情
suite.addTest(MyTestSuite("test_orders"))   # 订单列表
suite.addTest(MyTestSuite("test_logout"))   # 退出


# 执行测试
runner = unittest.TextTestRunner()
runner.run(suite)

# 测试执行时间计算
end_time = datetime.datetime.now()
total_use_case = u"执行用例总数:" + str(fs_util.num_success + fs_util.num_fail) + \
                 u"\t通过数:" + str(fs_util.num_success) + \
                 u"\t不通过数:" + str(fs_util.num_fail)
total_time = u"\t总共耗时：" + str((end_time-start_time).seconds) + u"秒"
print total_use_case + total_time

# 发生邮件测试报告
#Send_email.send_email(text)
