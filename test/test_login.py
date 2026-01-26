import allure
import pytest
from pageObjects.login import LoginPage
from pageObjects.search_product_page import SearchProductPage
from pageObjects.add_to_cart import AddToCart
from pageObjects.secure_checkoutPage import Secure_CheckoutPage
from pageObjects.shop_cart import ShopCartPage


class TestAmazonOrder:

    @pytest.mark.parametrize("email,password", [
        ("wrongmail.com", "WrongPass123"),
        ("g.sheakher@gmail.com", "Sarzzi@2023")
    ])
    def test_invalid_login(self, browserInstance, email, password):
        login = LoginPage(browserInstance)

        status = login.login(email, password)

        with allure.step("Verify login failure"):
            assert status in ["INVALID_EMAIL", "INVALID_PASSWORD"]

    @allure.feature("Login")
    @allure.story("Valid login and add to cart")
    def test_login_search_and_add_to_cart(self, browserInstance):
        driver = browserInstance
        login = LoginPage(driver)

        with allure.step("Login with valid credentials"):
            status = login.login("shekr@gmail.com", "Some@1990")
            assert status == "LOGIN_SUCCESS"

        with allure.step("Search for product"):
            search_page = SearchProductPage(driver)
            search_page.search_product("iphone 17 pro")
            search_page.click_first_product()
            print("Clicked on Search to search for the product")

        with allure.step("Switch to product window"):
            parent_window = driver.current_window_handle
            for window in driver.window_handles:
                if window != parent_window:
                    driver.switch_to.window(window)
                    break

        with allure.step("Add product to cart"):
            addToCart = AddToCart(driver)
            addToCart.add_to_cart()
            print("One Item added to the cart successfully!!!!")

        with allure.step("Check if product in cart more than 2"):
            count_product = ShopCartPage(driver)
            count_product.shopCart()
            count_product.get_item_details()

        with allure.step("When on Secure Checkout Page"):
            checkout = Secure_CheckoutPage(driver)
            checkout.get_CustomerDetails()
            checkout.add_delivery_instruction()




