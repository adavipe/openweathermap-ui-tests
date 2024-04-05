import allure
from pages.base_page import BasePage
from config.links import Links
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    locators = LoginPageLocators

    @allure.step("Enter login")
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL_FIELD)).send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.PASSWORD_FIELD)).send_keys(password)

    def click_remember_me_checkbox(self):
        pass

    @allure.step("Click submit button")
    def click_submit_button(self):
        # self.wait.until(EC.element_to_be_clickable(self.locators.SUBMIT_BUTTON)).click()
        self.find_element(self.locators.SUBMIT_BUTTON).click()



    @allure.step("Click on 'Create an Account' link")
    def click_create_account_link(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CREATE_ACCOUNT_LINK)).click()

    @allure.step("Click on 'Click here to recover' link")
    def click_recover_account_link(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.RECOVER_ACCOUNT_LINK)).click()
