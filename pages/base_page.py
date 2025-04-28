import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # ищем элемент с ожиданием
    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # кликаем по элементу
    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # вводим текст в поле
    @allure.step('Ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # получаем текс элемента
    @allure.step('Получение текста')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # изменение значения в локаторе
    @allure.step('Изменение локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return (method, locator)

    # Скрол до нужного элемента
    @allure.step('Скрол странички')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)












