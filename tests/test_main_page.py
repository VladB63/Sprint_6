import allure
import pytest
from data import UrlPage, AnswerBlock
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators




class TestMainPage:

    @allure.title('Проверка вопросов')
    @allure.step('Клик на вопрос')
    @pytest.mark.parametrize(
        'num', [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_click_question(self, driver, num):
        driver.get(UrlPage.SAMOKAT_URL)
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.SCROLL_TO_QUESTION)
        main_page.click_to_question(num)
        assert main_page.get_answer(num) == AnswerBlock.ANSWER_LIST[num]





