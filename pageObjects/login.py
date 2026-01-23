from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.signin_btn = (By.XPATH, "//span[contains(.,'Hello, sign in')]")
        self.email_txt = (By.ID, "ap_email_login")
        self.continue_btn = (By.ID, "continue")
        self.password_txt = (By.ID, "ap_password")
        self.submit_btn = (By.ID, "signInSubmit")

        self.invalid_email = (By.XPATH, "//div[contains(text(),'Invalid email address')]")
        self.password_error = (By.XPATH, "//div[@class='a-section a-spacing-base auth-pagelet-container']//div[@class='a-box-inner a-alert-container']//div[1]")

    def login(self, email, password):
        self.driver.get("https://www.amazon.in")
        self.driver.find_element(*self.signin_btn).click()

        self.wait.until(EC.visibility_of_element_located(self.email_txt)).send_keys(email)
        self.driver.find_element(*self.continue_btn).click()

        # 🔹 Case 1: Invalid email
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.invalid_email)
            )
            print("Invalid email detected")
            return "INVALID_EMAIL"
        except TimeoutException:
            pass  # email is valid → continue

        # 🔹 Case 2: Password screen
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.password_txt)
            ).send_keys(password)
            self.driver.find_element(*self.submit_btn).click()
        except TimeoutException:
            return "PASSWORD_FIELD_NOT_FOUND"

        # 🔹 Case 3: Invalid password
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.password_error)
            )
            print("Invalid password")
            return "INVALID_PASSWORD"
        except TimeoutException:
            pass

        return "LOGIN_SUCCESS"

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_msg)
        ).text
