import allure
from locators.Personal_account import PersonalAccount
from pages.Base_page import BasePage
from data import Data


class AccountPage(BasePage):
    @allure.step("Заполнение поля email")
    def fill_email(self):
        self.type_text(PersonalAccount.EMAIL_FIELD, Data.EMAIL)

    @allure.step("Заполнение поля пароля")
    def fill_password(self):
        self.type_text(PersonalAccount.PASSWORD_FIELD, Data.PASSWORD)

    @allure.step("Нажатие на кнопку входа")
    def login_button(self):
        self.click_element(PersonalAccount.SIGN_BUTTON_REGISTRATION_FORM)

    @allure.step("Переход в личный кабинет")
    def personal_account(self):
        self.wait_and_find_element(PersonalAccount.PERSONAL_ACCOUNT)
        self.click_element(PersonalAccount.PERSONAL_ACCOUNT)

    @allure.step("Переход в историю заказов")
    def click_history_orders(self):
        self.wait_and_find_element(PersonalAccount.HISTORY_ORDERS)
        self.click_element(PersonalAccount.HISTORY_ORDERS)

    @allure.step("Нажатие на кнопку выхода из аккаунта")
    def exit_button(self):
        self.wait_and_find_element(PersonalAccount.LOG_OUT)
        self.click_element(PersonalAccount.LOG_OUT)

    @allure.step("Отображение раздела Профиль")
    def profile_display(self):
        return self.wait_and_find_element(PersonalAccount.PROFILE)

    @allure.step("Отображение кнопки входа")
    def sign_button_display(self):
        return self.wait_and_find_element(PersonalAccount.SIGN_BUTTON_REGISTRATION_FORM)
