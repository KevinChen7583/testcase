import HTMLTestRunnerCN
import unittest
import time

#文件路径
#Testcase_dir = 'C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test'
#Testcase_dir='C:\pythonproject\UI_AutoTest\test_case'
# Testcase_dir="../ui_test"
Testcase_dir='../test_case'
#该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'testcase05.py')

#测试报告名称前加时间戳
#now=time.strftime("%Y-%m-%d %H_%M_%S")

# 定义报告存放路径
#filename = "C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\ui_autotest_result.html"
#filename = "C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\"+now+"ui_autotest_result.html"
#filename='C:\pythonproject\UI_AutoTest\test_case'now+'test_report.html'
filename="../test_case/test_report.html"

# 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")

# 运行测试用例
runner.run(dis)

#关闭报告文件
#fp.close()

