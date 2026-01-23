import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.get_no_items = (By.XPATH, "//span[@data-a-selector='inner-value']")
        self.decrease_quantity = (By.XPATH, "//button[@aria-label='Decrease quantity by one']")
        self.proceed_to_cart = (By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def shopCart(self):
        while True:
            count = int(
                self.wait.until(EC.visibility_of_element_located(self.get_no_items)).text
            )

            if count <= 1:
                break

            decrease_btn = self.wait.until(
                EC.element_to_be_clickable(self.decrease_quantity)
            )
            decrease_btn.click()
        self.driver.find_element(*self.proceed_to_cart).click()



