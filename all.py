import unittest

from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':

    suite=unittest.defaultTestLoader.discover('./test_page','*.py')
    report_file=open('./report/reports.html','wb')
    runner=HTMLTestRunner(stream=report_file, title='自动化测试', description='自动化测试描述')
    runner.run(suite)

