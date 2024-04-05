from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id="user_email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="user_password"]')
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, 'input[id="user_remember_me]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[value="Submit"]')
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/users/sign_up"]')
    RECOVER_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="#"]')
