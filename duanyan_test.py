import requests
import json
import unittest
class ymw(unittest.TestCase):
    def test01(self):
        url='http://localhost:8080/EasyBuy/Login'
        data='loginname=admin&password=123456&action=login'
        headers={
            "Content-Type":"application/x-www-from-urlencoded"
        }
        response=requests.post(url,headers=headers,params=data)
        #获取返回的结果
        print(response.json())
        #获取状态码
        result=response.json()['data']
        print(result)
        self.assertEqual('登陆成功',result)
        self.assertIn('1',response.text)
        self.assertTrue('操作成功'in response.text)

