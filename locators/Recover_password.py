from selenium.webdriver.common.by import By


class RecoveryPassword:
    EMAIL_FIELD = By.NAME, "name"
    PASSWORD_FIELD = By.XPATH, ".//input[@name='Введите новый пароль']"
    RECOVERY_PASSWORD = By.XPATH, "//a[text() = 'Восстановить пароль']" 
    RECOVER = By.XPATH, ".//button[text() = 'Восстановить']"
    SHOW_PASSWORD = By.XPATH, ".//div[@class='input__icon input__icon-action']"
    PASSWORD_ACTIVE = By.CSS_SELECTOR, ".input.input_status_active"
    BUTTON_SAVE = By.XPATH, ".//button[text()='Сохранить']"





