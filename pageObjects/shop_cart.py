import time
import pyperclip

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.get_no_items = (By.XPATH, "//span[@data-a-selector='inner-value']")
        self.decrease_quantity = (By.XPATH, "//button[@aria-label='Decrease quantity by one']")

        self.click_share = (By.XPATH, "//a[normalize-space()='Share']")
        self.share_link_input = (By.XPATH, "//input[@aria-label='Copy Link']")
        # self.close_sharePopUp = (By.XPATH, "//button[@aria-label='Close']")
        self.proceed_to_cart = (By.NAME, "proceedToRetailCheckout")

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

    def get_item_details(self):

        self.wait.until(EC.element_to_be_clickable(self.click_share)).click()
        print("Clicked on Share Link ")

        copy_btn = self.wait.until(
            EC.element_to_be_clickable(self.share_link_input)
        )
        copy_btn.click()

        time.sleep(3)  # let clipboard update
        share_link = pyperclip.paste()

        print("Share link:", share_link)
        self.driver.find_element(*self.proceed_to_cart).click()

