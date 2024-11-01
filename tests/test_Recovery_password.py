import allure
from locators.Stellar_burger_main import StellarBurger
from pages.Recovery_password_page import PasswordPage
from pages.Base_page import BasePage
from data import Url


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_transition_recovery_page(self, driver):
        stellar_burger = BasePage(driver)
        recovery_password_page = PasswordPage(driver)
        stellar_burger.click_element(StellarBurger.LOGIN_BUTTON)
        recovery_password_page.click_recovery_button()
        assert recovery_password_page.get_current_url() == f"{Url.RECOVER_PASSWORD}"

    @allure.title("Ввод почты и клик по кнопке «Восстановить")
    def test_enter_email_and_click_button(self, driver):
        stellar_burger = BasePage(driver)
        recovery_password_page = PasswordPage(driver)
        stellar_burger.click_element(StellarBurger.LOGIN_BUTTON)
        recovery_password_page.click_recovery_button()
        recovery_password_page.fill_email()
        recovery_password_page.click_recovery()
        assert recovery_password_page.save_button_display().text == "Сохранить"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_visibility_password(self, driver):
        stellar_burger = BasePage(driver)
        recovery_password_page = PasswordPage(driver)
        stellar_burger.click_element(StellarBurger.LOGIN_BUTTON)
        recovery_password_page.click_recovery_button()
        recovery_password_page.fill_email()
        recovery_password_page.click_recovery()
        recovery_password_page.fill_password()
        recovery_password_page.click_show_button()
        assert recovery_password_page.active_password_display()
