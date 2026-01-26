import allure
from pageObjects.search_product_page import SearchProductPage

@allure.feature("Search")
class TestProductSearch:

    def test_search_product(self, logged_in_user):
        driver = logged_in_user
        search_page = SearchProductPage(driver)

        with allure.step("Search for product"):
            search_page.search_product("iphone 17 pro")
            search_page.click_first_product()
