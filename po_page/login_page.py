import time

from selenium.webdriver.common.by import By

from venv.base_page.base import BasePage


class LoginPage(BasePage):
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "userpassword")
    selete_loc = (By.ID, 's2id_autogen1')
    back_loc=(By.XPATH,'//*[@id="select2-drop"]/div/input')
    botton_loc=(By.ID,'loginButton')


    move_loc = (By.LINK_TEXT, 'user')
    quit_loc = (By.LINK_TEXT, '退出')

    def login_ecshop(self, username, password,selector):
        self.send_Keys(LoginPage.username_loc, username)
        self.send_Keys(LoginPage.password_loc, password)
        self.send_Keys(LoginPage.selete_loc,selector)
        self.click(LoginPage.submit_loc)

    def get_except_result(self):
        self.locator_move_element(LoginPage.move_loc)
        time.sleep(1)
        return self.get_value(LoginPage.quit_loc)
