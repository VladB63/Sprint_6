import allure
import pytest
from data import UrlPage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators


class TestGoingPage:

    @allure.title('Проверка перехода по клику на лого Яндекса')
    def test_click_to_logo_ya(self, driver):
        main_page = MainPage(driver)
        main_page.open_url_samokat()
        main_page.click_to_logo_ya()
        main_page.switch_to_new_window()
        main_page.find_button_find()
        button_find = main_page.find_button_find()
        assert button_find.is_displayed()


    @allure.title('Проверка перехода по клику на лого Самоката')
    @pytest.mark.parametrize(
        "locator", [OrderPageLocators.BUTTON_ORDER_MINI,
                    OrderPageLocators.BUTTON_ORDER_BIG]
    )
    def test_click_to_logo_samokat(self,locator, driver):
        main_page = MainPage(driver)
        main_page.open_url_samokat()
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        main_page.click_to_logo_samokat()
        current_url = main_page.get_current_url()
        assert current_url == UrlPage.SAMOKAT_URL

