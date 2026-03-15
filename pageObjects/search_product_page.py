from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.search_field = (By.ID, "twotabsearchtextbox")
        self.search_btn = (By.ID, "nav-search-submit-button")
        self.first_product = (By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal']//h2[@aria-label='Sponsored Ad - iPhone 17 Pro 256 GB: 15.93 cm (6.3″) Display with Promotion up to 120Hz, A19 Pro Chip, Breakthrough Battery Life, Pro Fusion Camera System with Center Stage Front Camera; Deep Blue']//span[contains(text(),'iPhone 17 Pro 256 GB: 15.93 cm (6.3″) Display with')]")

    def search_product(self, product):
        self.wait.until(
            EC.visibility_of_element_located(self.search_field)
        ).send_keys(product)

        self.driver.find_element(*self.search_btn).click()

    def click_first_product(self):
        self.driver.find_element(*self.first_product).click()



