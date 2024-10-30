from locators.Recover_password import RecoveryPassword
from pages.Stellar_Burger_page import PageStellarBurger
from data import Data


class Password(PageStellarBurger):

    def click_recovery_button(self):
        self.wait_and_find_element(RecoveryPassword.RECOVERY_PASSWORD)
        self.click_element(RecoveryPassword.RECOVERY_PASSWORD)

    def fill_email(self):
        self.type_text(RecoveryPassword.EMAIL_FIELD, Data.EMAIL)

    def click_recovery(self):
        self.click_element(RecoveryPassword.RECOVER)

    def fill_password(self):
        self.wait_and_find_element(RecoveryPassword.PASSWORD_FIELD)
        self.type_text(RecoveryPassword.PASSWORD_FIELD, Data.PASSWORD)

    def click_show_button(self):
        self.click_element(RecoveryPassword.SHOW_PASSWORD)

    def password_visible(self):
        self.check_element_display(RecoveryPassword.PASSWORD_ACTIVE)

    def save_button_display(self):
        return self.wait_and_find_element(RecoveryPassword.BUTTON_SAVE)

    def active_password_display(self):
        return self.wait_and_find_element(RecoveryPassword.PASSWORD_ACTIVE)

