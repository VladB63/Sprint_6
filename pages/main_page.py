import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.going_page_locators import GoingPageLocators
from data import UrlPage



class MainPage(BasePage):

    @allure.step('Переход по урлу')
    def open_url_samokat(self):
        self.go_to_url(UrlPage.SAMOKAT_URL)


    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_format = self.format_locators(MainPageLocators.PANEL_QUESTION, num)
        self.scroll_to_element(MainPageLocators.SCROLL_TO_QUESTION)
        self.click_to_element(locator_format)


    @allure.step('Получение ответа')
    def get_answer(self, num):
        locator_format = self.format_locators(MainPageLocators.PANEL_ANSWER, num)
        return self.get_text_from_element(locator_format)


    @allure.step('Клик лого Яндекс')
    def click_to_logo_ya(self):
        self.click_to_element(GoingPageLocators.LOGO_BUTTON_YA)


    @allure.step('Клик лого Самокат')
    def click_to_logo_samokat(self):
        self.click_to_element(GoingPageLocators.LOGO_BUTTON_SAMOKAT)


    @allure.step('Клик кнопки заказать на главной страницы')
    def click_button_order(self, locator):
        self.find_element_with_wait(locator)
        self.scroll_to_element(locator)
        self.click_to_element(locator)


    @allure.step('Получение кнопки Найти на страничке Дзен')
    def find_button_find(self):
        return self.find_element_with_wait(GoingPageLocators.DZEN_BUTTON_FIND)



