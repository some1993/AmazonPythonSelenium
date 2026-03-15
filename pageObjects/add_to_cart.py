import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddToCart:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.cart_btn = (By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//div[@id='addToCart_feature_div']//div//input[@id='add-to-cart-button']")
        self.final_cart = (By.XPATH, "//span[@class='a-button a-button-primary attach-button-large attach-primary-cart-button']//input[@type='submit']")
        self.price = (By.XPATH, "//span[normalize-space()='1,34,900']")
        self.submit_btn = (By.XPATH, "//span[@class='a-button a-button-primary attach-button-large attach-primary-cart-button']//input[@type='submit']")
        self.back_to_cart = (By.XPATH, "//a[normalize-space()='Back to cart']")

    def add_to_cart(self):

        iphone_price = self.driver.find_element(*self.price).text
        print(f"Price of the iphone 16 pro ", iphone_price)
        btn = self.wait.until(EC.presence_of_element_located(self.cart_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.wait.until(EC.element_to_be_clickable(self.cart_btn)).click()
        self.driver.find_element(*self.final_cart).click()
        time.sleep(2)

    def click_to_cart(self):
        self.driver.find_element(*self.submit_btn).click()
        print("Able to click on Proceed to Cart")
        self.driver.find_element(*self.back_to_cart).click()
        print("Clicked on back to cart")