import unittest

from base_page.Base_Util import BaseUtil
from po_page.Login import LoginPage
import LoginPage
import time


class TestCase(BaseUtil):

    def test_01_login(self):
        lp=LoginPage(self.driver)
        lp.login_ecshop('user','password')
        #断言判断是否符合结果
        time.sleep(1)
        self.assertEqual(lp.get_except_result(),'退出') #判断两个值是否相等
       # self.assertTrue()#判断一个值是否为True
        #self.assertIn()#判断一个值是否在另一个值里面