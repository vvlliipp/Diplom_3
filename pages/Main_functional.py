from locators.Stellar_burger_main import StellarBurger
from locators.Order_feed import OrderFeed
from pages.Stellar_Burger_page import PageStellarBurger


class Main(PageStellarBurger):
    def click_constructor(self):
        self.wait_and_find_element(StellarBurger.CONSTRUCTOR)
        self.click_element(StellarBurger.CONSTRUCTOR)

    def click_order_feed(self):
        self.wait_and_find_element(StellarBurger.ORDER_FEED)
        self.click_element(StellarBurger.ORDER_FEED)

    def click_bun(self):
        self.wait_and_find_element(StellarBurger.BUN_1)
        self.click_element(StellarBurger.BUN_1)

    def ingredient_details(self):
        self.wait_and_find_element(OrderFeed.DETAILS_INGREDIENT)
        self.check_element_display(OrderFeed.DETAILS_INGREDIENT)

    def ingredients_details_display(self):
        return self.wait_and_find_element(OrderFeed.DETAILS_INGREDIENT)

    def close_details(self):
        self.wait_and_find_element(OrderFeed.CLOSE_DETAILS)
        self.click_element(OrderFeed.CLOSE_DETAILS)

    def drug_the_bun(self):
        self.drag_and_drop_elements(StellarBurger.BUN_1, StellarBurger.DRUG_BUN_1)

    def counter(self):
        return self.get_element_text(OrderFeed.ORDER_COUNTER)

    def click_place_on_order(self):
        self.wait_and_find_element(StellarBurger.PLACE_ON_ORDER)
        self.click_element(StellarBurger.PLACE_ON_ORDER)

    def click_login_account(self):
        self.click_element(StellarBurger.LOGIN_BUTTON)

    def build_burger_page_display(self):
        return self.wait_and_find_element(StellarBurger.BURGER_BUILD_PAGE)

    def check_el_order_start(self):
        return self.wait_and_find_element(OrderFeed.ORDER_START)

    def sleep_wait_close_details(self):
        self.sleep(OrderFeed.CLOSE_DETAILS)


