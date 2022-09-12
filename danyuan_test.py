import requests
import json
import unittest
import HTMLTestRunnerCN
class inter_test(unittest.TestCase):
    #获取实时天气接口
    def test01(self):
        url='https://tianqiapi.com/api?version=v6&appid=73691227&appsecret=123456'
        response=requests.get(url)
        print(json.dumps(response.json(),indent=4,ensure_ascii=False))

    # @unittest.skip('不执行此用例')
    #  #获取易买网登录接口
    # def test02(self):
    #     url='http://localhost:8080/EasyBuy/Login'
    #     data='loginname=admin&password=123456&action=login'
    #     response=requests.post(url,params=data)
    #     print(json.dumps(response.json(),indent=4,ensure_ascii=False))

# if __name__ == '__main__':
#     #unittest.main
#     suite=unittest.TestSuite()
#     suite.addTest(inter_test('test01'))
#     unittest.TextTestRunner().run(suite)





