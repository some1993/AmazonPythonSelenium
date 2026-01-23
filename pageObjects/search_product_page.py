from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.search_field = (By.ID, "twotabsearchtextbox")
        self.search_btn = (By.ID, "nav-search-submit-button")
        self.first_product = (By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")

    def search_product(self, product):
        self.wait.until(
            EC.visibility_of_element_located(self.search_field)
        ).send_keys(product)

        self.driver.find_element(*self.search_btn).click()

    def click_first_product(self):
        self.driver.find_element(*self.first_product).click()


