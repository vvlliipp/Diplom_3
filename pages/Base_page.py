import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Вводим текст в элемент")
    def type_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Получаем текст элемента")
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return element.text

    @allure.step("Ожидаем видимость и кликабельность элемента")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Проверяем отображение элемента")
    def check_element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Скролл до элемента")
    def get_visible_elements_with_scroll(self, locator, timeout=15):
        elements = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))
        visible_elements = []
        for element in elements:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
            if element.is_displayed():
                visible_elements.append(element)
        return visible_elements

    @allure.step("Кликаем на элемент")
    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step("Ожидание обновления текста элемента")
    def wait_text_element_new(self, locator, text, time=5):
        return WebDriverWait(self.driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step("Перетаскивание элемента")
    def drag_and_drop_elements(self, source_locator, target_locator):
        source = self.wait_and_find_element(source_locator)
        target = self.wait_and_find_element(target_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @allure.step("Ожидание элемента с задержкой")
    def sleep(self, locator):
        time.sleep(5)
        self.wait_and_find_element(locator)
