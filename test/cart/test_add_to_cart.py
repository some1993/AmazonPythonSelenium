import allure
from pageObjects.add_to_cart import AddToCart
from pageObjects.search_product_page import SearchProductPage
from pageObjects.shop_cart import ShopCartPage

@allure.feature("Cart")
class TestAddToCart:

    def test_add_product_to_cart(self, logged_in_user):
        driver = logged_in_user

        search_page = SearchProductPage(driver)
        search_page.search_product("iphone 17 pro")
        search_page.click_first_product()

        parent = driver.current_window_handle
        for win in driver.window_handles:
            if win != parent:
                driver.switch_to.window(win)
                break

        add_to_cart = AddToCart(driver)
        add_to_cart.add_to_cart()
