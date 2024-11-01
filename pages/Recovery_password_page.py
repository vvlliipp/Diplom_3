import allure
from locators.Recover_password import RecoveryPassword
from pages.Base_page import BasePage
from data import Data


class PasswordPage(BasePage):
    @allure.step("Нажатие на кнопку восстановления пароля")
    def click_recovery_button(self):
        self.wait_and_find_element(RecoveryPassword.RECOVERY_PASSWORD)
        self.click_element(RecoveryPassword.RECOVERY_PASSWORD)

    @allure.step("Заполнение поля email для восстановления пароля")
    def fill_email(self):
        self.type_text(RecoveryPassword.EMAIL_FIELD, Data.EMAIL)

    @allure.step("Нажатие на кнопку Восстановить")
    def click_recovery(self):
        self.click_element(RecoveryPassword.RECOVER)

    @allure.step("Заполнение поля нового пароля")
    def fill_password(self):
        self.wait_and_find_element(RecoveryPassword.PASSWORD_FIELD)
        self.type_text(RecoveryPassword.PASSWORD_FIELD, Data.PASSWORD)

    @allure.step("Нажатие на кнопку показа пароля")
    def click_show_button(self):
        self.click_element(RecoveryPassword.SHOW_PASSWORD)

    @allure.step("Отображение пароля")
    def password_visible(self):
        self.check_element_display(RecoveryPassword.PASSWORD_ACTIVE)

    @allure.step("Отображение кнопки сохранения")
    def save_button_display(self):
        return self.wait_and_find_element(RecoveryPassword.BUTTON_SAVE)

    @allure.step("Отображение поля пароль как активное")
    def active_password_display(self):
        return self.wait_and_find_element(RecoveryPassword.PASSWORD_ACTIVE)

