from locators.Personal_account import PersonalAccount
from pages.Stellar_Burger_page import PageStellarBurger
from data import Data


class Account(PageStellarBurger):

    def fill_email(self):
        self.type_text(PersonalAccount.EMAIL_FIELD, Data.EMAIL)

    def fill_password(self):
        self.type_text(PersonalAccount.PASSWORD_FIELD, Data.PASSWORD)

    def login_button(self):
        self.click_element(PersonalAccount.SIGN_BUTTON_REGISTRATION_FORM)

    def personal_account(self):
        self.wait_and_find_element(PersonalAccount.PERSONAL_ACCOUNT)
        self.click_element(PersonalAccount.PERSONAL_ACCOUNT)

    def click_history_orders(self):
        self.wait_and_find_element(PersonalAccount.HISTORY_ORDERS)
        self.click_element(PersonalAccount.HISTORY_ORDERS)

    def exit_button(self):
        self.wait_and_find_element(PersonalAccount.LOG_OUT)
        self.click_element(PersonalAccount.LOG_OUT)

    def profile_display(self):
        return self.wait_and_find_element(PersonalAccount.PROFILE)

    def sign_button_display(self):
        return self.wait_and_find_element(PersonalAccount.SIGN_BUTTON_REGISTRATION_FORM)
