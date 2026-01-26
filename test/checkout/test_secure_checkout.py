import allure

from pageObjects.add_to_cart import AddToCart
from pageObjects.search_product_page import SearchProductPage
from pageObjects.secure_checkoutPage import Secure_CheckoutPage
from pageObjects.shop_cart import ShopCartPage


@allure.feature("Checkout")
class TestSecureCheckout:

    def test_secure_checkout_page(self, logged_in_user):
        driver = logged_in_user

        # Search product
        search = SearchProductPage(driver)
        search.search_product("iphone 17 pro")
        search.click_first_product()

        # Switch window
        parent = driver.current_window_handle
        for win in driver.window_handles:
            if win != parent:
                driver.switch_to.window(win)
                break

        # Add to cart
        add_to_cart = AddToCart(driver)
        add_to_cart.add_to_cart()

        # Go to cart
        cart = ShopCartPage(driver)
        cart.shopCart()
        cart.get_item_details()


        # NOW we are on Secure Checkout
        checkout = Secure_CheckoutPage(driver)
        checkout.get_CustomerDetails()
        checkout.add_delivery_instruction()
