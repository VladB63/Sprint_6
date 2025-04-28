import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_format = self.format_locators(MainPageLocators.PANEL_QUESTION, num)
        self.scroll_to_element(MainPageLocators.SCROLL_TO_QUESTION)
        self.click_to_element(locator_format)


    @allure.step('Получение ответа')
    def get_answer(self, num):
        locator_format = self.format_locators(MainPageLocators.PANEL_ANSWER, num)
        return self.get_text_from_element(locator_format)


    @allure.step('Клик лого для перехода')
    def click_to_logo(self, locator):
        self.click_to_element(locator)


    @allure.step('Клик кнопки заказать на главной страницы')
    def click_button_order(self, locator):
        self.click_to_element(locator)










