import allure
from pages.Main_functional_page import MainPage
from pages.Personal_account_page import AccountPage
from pages.Order_page import OrderPage


class TestOrderFeedFunctionality:
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_details_popup(self, driver):
        order_page = OrderPage(driver)
        main = MainPage(driver)
        main.click_order_feed()
        order_page.click_order_in_feed()
        assert order_page.composition_order_display().text == "Cостав"

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_find_order_in_feed(self, driver):
        order_page = OrderPage(driver)
        account_page = AccountPage(driver)
        main = MainPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        main.drug_the_bun()
        main.click_place_on_order()
        main.sleep_wait_close_details()
        main.close_details()
        account_page.personal_account()
        account_page.click_history_orders()
        order_number = order_page.get_last_order()
        main.click_order_feed()
        assert order_number in order_page.get_number_of_orders()

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_total_orders_count_increment(self, driver):
        order_page = OrderPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        main_page.click_order_feed()
        initial_count = order_page.get_total_orders_count()
        main_page.click_constructor()
        main_page.drug_the_bun()
        main_page.click_place_on_order()
        main_page.sleep_wait_close_details()
        main_page.close_details()
        main_page.click_order_feed()
        updated_count = order_page.get_total_orders_count()
        assert updated_count == initial_count + 1

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_orders_count_increment(self, driver):
        order_page = OrderPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        main_page.click_order_feed()
        order_page.scroll_orders_today()
        initial_count = order_page.get_today_orders_count()
        main_page.click_constructor()
        main_page.drug_the_bun()
        main_page.click_place_on_order()
        main_page.sleep_wait_close_details()
        main_page.close_details()
        main_page.click_order_feed()
        order_page.scroll_orders_today()
        updated_count = order_page.get_today_orders_count()
        assert updated_count == initial_count + 1

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_in_work(self, driver):
        order_page = OrderPage(driver)
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        main_page.drug_the_bun()
        main_page.click_place_on_order()
        order_number = order_page.get_updated_order_number()
        main_page.sleep_wait_close_details()
        main_page.close_details()
        main_page.click_order_feed()
        order_number_in_work = order_page.get_in_work_order_number()
        assert f"0{order_number}" in order_number_in_work
