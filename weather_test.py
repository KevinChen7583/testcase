import requests
import json
import unittest
import HTMLTestRunnerCN

class inter_test(unittest.TestCase):
    #获取实时天气
    def test01(self):
        url='https://tianqiapi.com/api'
        data='version=v6&appid=73691227&appsecret=123456'
        response=requests.get(url,params=data)
        print(json.dumps(response.json(),indent=4,ensure_ascii=False))

#文件路径
Testcase_dir='../api_test'
# 'C:\pythonproject\UI_AutoTest\Api-package'
#测试报告名称前加时间戳
# now=time.strftime('%Y-%m-%d %H_%M_%S')

#获取读取文件
dis=unittest.defaultTestLoader.discover(Testcase_dir,'weather_test.py')

#存放报告的路径
filename='../api_test/weather_report.html'

fp=open(filename,'wb')

runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='接口测试报告',description='用例执行情况')

runner.run(dis)

fp.close()




