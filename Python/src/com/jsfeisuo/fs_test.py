#!/usr/bin/python
# -*- coding:utf-8 -*
import sys
sys.path.append('/usr/local/lib/python2.7')
import requests
import unittest
import json
from fs_util import test_result

header = {'Content-Type': 'application/json'}
url = "http://192.168.11.19:8085/api/v1.0/aps"
oid = ''
uid = 0
code = 200
class MyTestSuite(unittest.TestCase):

    #测试查询站点的接口
    def test_stations(self):
        realUrl = url+"/station/stations"
        datas = {'elongitude': "120.10", 'wlongitude': "120.02", 'nlatitude': "31.99", 'slatitude': "31.90"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        test_result(r,code)

    #测试查询路网的接口
    def test_edge(self):
        realUrl = url + "/station/edges"
        datas  = {'elongitude': "120.10", 'wlongitude': "120.02", 'nlatitude': "31.99", 'slatitude': "31.90"}
        r = requests.post(realUrl,headers = header,data=json.dumps(datas))
        test_result(r,code)

    #测试查询路网的接口
    def test_completion(self):
        realUrl = url + "/station/completion"
        datas  = {"city": '',"keyword":"飞","page":"1","size":"10"}
        r = requests.post(realUrl,headers = header,data=json.dumps(datas))
        test_result(r,code)

    def test_authcode(self):
        realUrl = url + "/common/authcod"
        r = requests.get(realUrl,params='18888106906')
        test_result(r,code)


    #测试登录的接口
    def test_login(self):
        global header
        global uid
        realUrl = url + "/user/login"
        datas = {"username":"18888106906","passwd":"123456"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        response = r.json()
        header['token'] = response['token']
        uid = response['uid']
        test_result(r,code)

    #测试获取个人信息的接口
    def test_user_info(self):
        realUrl = url + "/user/info/"+ str(uid)
        r = requests.get(realUrl,headers=header)
        test_result(r,code)

    #测试获取余额的接口
    def test_balance(self):
        realUrl = url + "/user/balance/"+ str(uid)
        r = requests.get(realUrl,headers=header)
        test_result(r,code)

    #测试修改密码的接口
    def test_update_passwd(self):
        realUrl = url + "/user/passwd"
        datas = {"uid":"10","passwd":"123456","newPasswd":"123456"}
        r = requests.put(realUrl,headers=header,data=json.dumps(datas))
        test_result(r,code)

    #测试获取预估路线的接口
    def test_estimation(self):
        realUrl = url + "/order/estimation"
        datas = {"deptId":"1","destId":"5"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        test_result(r,code)
        
    #测试创建订单的接口
    def test_order(self):
        global oid
        realUrl = url + "/order"
        datas = {"deptId":"1","destId":"5"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        response = r.json()
        oid = response["id"]
        test_result(r,code)

    #测试支付订单的接口
    def test_payment(self):
        realUrl = url + "/order/payment"
        datas = {"oid":oid,"ptype":"5","amount":"500"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        test_result(r,code)

    #测试获取订单详情的接口
    def test_detail(self):
        realUrl = url + "/order/" + str(oid)
        r = requests.get(realUrl,headers=header)
        test_result(r,code)

    #测试获取订单列表的接口
    def test_orders(self):
        realUrl = url + "/order/orders"
        datas = {"status":"","page":"1","size":"10"}
        r = requests.post(realUrl,headers=header,data=json.dumps(datas))
        test_result(r,code)

    #测试退出登录的接口
    def test_logout(self):
        realUrl = url + "/user/logout/" + str(uid)
        r = requests.get(realUrl,headers=header)
        test_result(r,code)



