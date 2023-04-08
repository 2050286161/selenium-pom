import unittest
from selenium import webdriver


class BaseUtil(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        # option = webdriver.ChromeOptions()
        # option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome()
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #            Object.defineProperty(navigator, 'webdriver', {
        #              get: () => undefined
        #            })
        #          """
        # })
        driver=self.driver
        self.driver.get('http://10.8.78.23:8002/heren/security/login.html')

    def tearDown(self) -> None:
        pass