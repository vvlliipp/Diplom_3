import allure
from locators.Order_feed import OrderFeed
from pages.Base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Клик на заказ в ленте заказов")
    def click_order_in_feed(self):
        self.click_element(OrderFeed.ORDER_IN_FEED)

    @allure.step("Получение количества заказов выполненных за всё время")
    def get_total_orders_count(self):
        total_orders = self.get_element_text(OrderFeed.ORDERS_ALL)
        return int(total_orders)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        today_orders = self.get_element_text(OrderFeed.ORDERS_DAY)
        return int(today_orders)

    @allure.step("Получение номера заказа после создания")
    def get_updated_order_number(self):
        self.wait_and_find_element(OrderFeed.ORDER_NUMBER)
        self.wait_text_element_new(OrderFeed.ORDER_NUMBER, "9999")
        return self.get_element_text(OrderFeed.ORDER_NUMBER)

    @allure.step("Получение номера заказа в разделе В работе")
    def get_in_work_order_number(self):
        self.wait_and_find_element(OrderFeed.ORDERS_IN_WORK)
        self.wait_text_element_new(OrderFeed.ORDERS_IN_WORK, "Все текущие заказы готовы!")
        return self.get_element_text(OrderFeed.ORDERS_IN_WORK)

    @allure.step("Отображение элемента Состав")
    def composition_order_display(self):
        self.sleep(OrderFeed.COMPOSITION_OF_ORDER)
        return self.wait_and_find_element(OrderFeed.COMPOSITION_OF_ORDER)

    @allure.step("Получение последнего заказа")
    def get_last_order(self):
        return self.wait_and_find_element(OrderFeed.LAST_ORDER).text

    @allure.step("Получение номера заказов")
    def get_number_of_orders(self):
        return self.wait_and_find_element(OrderFeed.NUMBER_OF_ORDER).text.splitlines()

    @allure.step("Прокрутка до элемента заказы за сегодня")
    def scroll_orders_today(self):
        self.wait_and_find_element(OrderFeed.ORDERS_DAY)
        self.get_visible_elements_with_scroll(OrderFeed.ORDERS_DAY)

