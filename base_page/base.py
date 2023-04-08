from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 定位元素关键字
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    #鼠标移动事件
    def locator_move_element(self, loc):
        return ActionChains(self.driver).move_to_element(self.locator_element(loc)).perform()

    # 设置值的关键字
    def send_Keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 鼠标点击事件
    def click(self, loc):
        self.locator_element(loc).click()

    #enter事件
    def submit(self, loc):
        self.locator_element(loc).send_keys(Keys.ENTER)
    #断言
    def get_value(self, loc):
        return self.locator_element(loc).text

    #删除一个字符
    def back_space(self,loc):
        self.locator_element(loc).send_key(Keys.BACK_SPACE)
