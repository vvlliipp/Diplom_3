import allure
from pages.Personal_account_page import AccountPage
from data import Url


class TestPersonalAccount:
    @allure.title("Переход по клику на «Личный кабинет»")
    def test_transition_to_personal_account(self, driver):
        account_page = AccountPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        account_page.personal_account()
        assert account_page.profile_display().text == "Профиль"

    @allure.title("Переход в раздел «История заказов»")
    def test_transition_to_order_history(self, driver):
        account_page = AccountPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        account_page.personal_account()
        account_page.click_history_orders()
        assert account_page.get_current_url() == f"{Url.ACCOUNT_HISTORY}"

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver):
        account_page = AccountPage(driver)
        account_page.personal_account()
        account_page.fill_email()
        account_page.fill_password()
        account_page.login_button()
        account_page.personal_account()
        account_page.exit_button()
        assert account_page.sign_button_display().text == "Войти"

