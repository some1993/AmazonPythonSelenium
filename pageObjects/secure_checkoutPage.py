import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Secure_CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_address = (By.XPATH, "//span[@id='deliver-to-address-text']")
        self.get_cards = (By.XPATH, "//div[@class='a-section a-spacing-none']//div[@class='a-box pmts-instrument-box']")
        self.click_delivery = (By.XPATH, "//a[normalize-space()='Add delivery instructions']")
        self.add_instruction = (By.XPATH, "//textarea[@id='freeTextInstruction-HOUSE']")
        self.save_instruction = (By.XPATH, "//input[@aria-labelledby='cdp-save-button-announce']")

    def get_CustomerDetails(self):
        # Print address
        print("Current Delivery Address ", self.driver.find_element(*self.get_address).text)

        # Get all card elements
        cards = self.driver.find_elements(*self.get_cards)

        card_values = []
        print(f"All the Payment Option Available are: ")
        for card in cards:
            text = card.text.strip()
            card_values.append(text)
            print(text)

    def add_delivery_instruction(self):

        self.driver.find_element(*self.click_delivery).click()
        self.driver.find_element(*self.add_instruction).send_keys("Take a approval from No broker or leave at security gate")
        self.driver.find_element(*self.save_instruction).click()
        print("Instruction added successfully")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']").click()









