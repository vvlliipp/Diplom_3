from selenium.webdriver.common.by import By


class PersonalAccount:
    PERSONAL_ACCOUNT = By.XPATH, "//p[text() = 'Личный Кабинет']"
    NAME_FIELD = By.XPATH, "//label[text() = 'Имя']/..//input"
    EMAIL_FIELD = By.XPATH, "//label[text() = 'Email']/..//input"
    PASSWORD_FIELD = By.NAME, "Пароль"
    SIGN_BUTTON_REGISTRATION_FORM = By.XPATH, "//button[text() = 'Войти']"
    PROFILE = By.XPATH, "//a[text() = 'Профиль']"
    LOG_OUT = By.XPATH, "//button[text() = 'Выход']"
    HISTORY_ORDERS = By.XPATH, "//a[text() = 'История заказов']"


