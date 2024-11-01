from selenium.webdriver.common.by import By


class OrderFeed:
    DETAILS_INGREDIENT = By.XPATH, ".//h2[text()='Детали ингредиента']"
    CLOSE_DETAILS = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    ORDER_IN_FEED = By.XPATH, './/*[contains(@class, "OrderHistory_link")]'
    ORDERS_ALL = By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"
    ORDERS_DAY = By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]"
    ORDERS_IN_WORK = By.XPATH, "//*[contains(@class, '_orderListReady')]/li"
    ORDER_COUNTER = By.XPATH, "//*[contains(@class, 'counter_counter__num')]"
    COMPOSITION_OF_ORDER = By.XPATH, ".//p[text()='Cостав']"
    LAST_ORDER = By.XPATH, './/li[last()]/a[contains(@href, "order-history")]/*/p[1]'
    ORDER_START = By.XPATH, ".//p[text()='Ваш заказ начали готовить']"
    NUMBER_OF_ORDER = By.XPATH, "//*[contains(text(), '#')]"
    ORDER_LIST = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    ORDER_NUMBER = By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text ""text_type_digits-large mb-8']"





