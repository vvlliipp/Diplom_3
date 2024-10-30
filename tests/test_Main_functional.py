import allure
from pages.Main_functional import Main
from pages.Personal_account_page import Account
from data import Url


class TestMainFunctionality:
    @allure.title("Переход по клику на «Конструктор»")
    def test_transition_to_constructor(self, driver):
        main_page = Main(driver)
        main_page.click_constructor()
        assert main_page.build_burger_page_display().text == "Соберите бургер"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_transition_to_order_feed(self, driver):
        main_page = Main(driver)
        main_page.click_order_feed()
        assert main_page.get_current_url() == f"{Url.ORDER_FEED}"

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_details_popup(self, driver):
        main_page = Main(driver)
        main_page.click_constructor()
        main_page.click_bun()
        main_page.ingredient_details()
        assert main_page.ingredients_details_display().text == "Детали ингредиента"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details(self, driver):
        main_page = Main(driver)
        main_page.click_bun()
        main_page.ingredient_details()
        main_page.close_details()
        assert main_page.build_burger_page_display().text == "Соберите бургер"

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter_increment(self, driver):
        main_page = Main(driver)
        main_page.drug_the_bun()
        assert main_page.counter() == '2'

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_placement_by_logged_in_user(self, driver):
        main_page = Main(driver)
        account = Account(driver)
        main_page.click_login_account()
        account.fill_email()
        account.fill_password()
        account.login_button()
        main_page.drug_the_bun()
        main_page.click_place_on_order()
        assert main_page.check_el_order_start().text == 'Ваш заказ начали готовить'
