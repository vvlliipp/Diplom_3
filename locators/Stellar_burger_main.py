from selenium.webdriver.common.by import By


class StellarBurger:
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text() = 'Личный Кабинет']"
    CONSTRUCTOR = By.XPATH, "//p[text() = 'Конструктор']"
    ORDER_FEED = By.XPATH, "//p[text() = 'Лента Заказов']"
    BURGER_BUILD_PAGE = By.XPATH, "//h1[text() = 'Соберите бургер']"
    LOGO_STELLAR_BURGER = By.CLASS_NAME, "AppHeader_header__logo"
    BREAD_SECTION = By.XPATH, "//span[text() = 'Булки']"
    BUN_1 = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"
    SELECTED_SECTION = By.XPATH, "[contains(@class, 'current')]"
    SAUCES_SECTION = By.XPATH, "//span[text() = 'Соусы']"
    FILLING_SECTION = By.XPATH, "//span[text() = 'Начинки']"
    PLACE_ON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"
    ID_ORDER = By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text ""text_type_digits-large mb-8']"
    DRUG_BUN_1 = By.XPATH, './/*[text()="Перетяните булочку сюда (верх)"]'






