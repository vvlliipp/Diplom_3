import allure
from locators.Stellar_burger_main import StellarBurger
from locators.Order_feed import OrderFeed
from pages.Base_page import BasePage


class MainPage(BasePage):
    @allure.step("Клик на конструктор")
    def click_constructor(self):
        self.wait_and_find_element(StellarBurger.CONSTRUCTOR)
        self.click_element(StellarBurger.CONSTRUCTOR)

    @allure.step("Клик на ленту заказов")
    def click_order_feed(self):
        self.wait_and_find_element(StellarBurger.ORDER_FEED)
        self.click_element(StellarBurger.ORDER_FEED)

    @allure.step("Клик на булочку")
    def click_bun(self):
        self.wait_and_find_element(StellarBurger.BUN_1)
        self.click_element(StellarBurger.BUN_1)

    @allure.step("Элемент Детали ингредиента отображается")
    def ingredients_details_display(self):
        return self.wait_and_find_element(OrderFeed.DETAILS_INGREDIENT)

    @allure.step("Закрытие окна Детали ингредиента")
    def close_details(self):
        self.wait_and_find_element(OrderFeed.CLOSE_DETAILS)
        self.click_element(OrderFeed.CLOSE_DETAILS)

    @allure.step("Перетаскивание булочки")
    def drug_the_bun(self):
        self.drag_and_drop_elements(StellarBurger.BUN_1, StellarBurger.DRUG_BUN_1)

    @allure.step("Получение значения счетчика")
    def counter(self):
        return self.get_element_text(OrderFeed.ORDER_COUNTER)

    @allure.step("Клик на кнопку оформления заказа")
    def click_place_on_order(self):
        self.wait_and_find_element(StellarBurger.PLACE_ON_ORDER)
        self.click_element(StellarBurger.PLACE_ON_ORDER)

    @allure.step("Клик на кнопку входа в аккаунт")
    def click_login_account(self):
        self.click_element(StellarBurger.LOGIN_BUTTON)

    @allure.step("Отображение страницы конструктора бургера")
    def build_burger_page_display(self):
        return self.wait_and_find_element(StellarBurger.BURGER_BUILD_PAGE)

    @allure.step("Отображение элемента Ваш заказ начали готовить")
    def check_el_order_start(self):
        return self.wait_and_find_element(OrderFeed.ORDER_START)

    @allure.step("Ожидание закрытия деталей ингредиента с задержкой")
    def sleep_wait_close_details(self):
        self.sleep(OrderFeed.CLOSE_DETAILS)


