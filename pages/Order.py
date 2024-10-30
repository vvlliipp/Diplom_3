from locators.Order_feed import OrderFeed
from pages.Stellar_Burger_page import PageStellarBurger


class Order(PageStellarBurger):

    def click_order_in_feed(self):
        self.click_element(OrderFeed.ORDER_IN_FEED)

    def get_order_number(self):
        return self.get_element_text(OrderFeed.DETAILS_INGREDIENT)

    def get_total_orders_count(self):
        total_orders = self.get_element_text(OrderFeed.ORDERS_ALL)
        return int(total_orders)

    def get_today_orders_count(self):
        today_orders = self.get_element_text(OrderFeed.ORDERS_DAY)
        return int(today_orders)

    def get_updated_order_number(self):
        self.wait_and_find_element(OrderFeed.ORDER_NUMBER)
        self.wait_text_element_new(OrderFeed.ORDER_NUMBER, "9999")
        return self.get_element_text(OrderFeed.ORDER_NUMBER)

    def get_in_work_order_number(self):
        self.wait_and_find_element(OrderFeed.ORDERS_IN_WORK)
        self.wait_text_element_new(OrderFeed.ORDERS_IN_WORK, "Все текущие заказы готовы!")
        return self.get_element_text(OrderFeed.ORDERS_IN_WORK)

    def composition_order_display(self):
        self.sleep(OrderFeed.COMPOSITION_OF_ORDER)
        return self.wait_and_find_element(OrderFeed.COMPOSITION_OF_ORDER)

    def get_last_order(self):
        return self.wait_and_find_element(OrderFeed.LAST_ORDER).text

    def get_number_of_orders(self):
        return self.wait_and_find_element(OrderFeed.NUMBER_OF_ORDER).text.splitlines()

    def scroll_orders_today(self):
        self.wait_and_find_element(OrderFeed.ORDERS_DAY)
        self.get_visible_elements_with_scroll(OrderFeed.ORDERS_DAY)

