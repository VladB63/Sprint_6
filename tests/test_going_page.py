import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import UrlPage
from pages.main_page import MainPage
from locators.going_page_locators import GoingPageLocators
from locators.order_page_locators import OrderPageLocators



class TestGoingPage:

    @allure.title('Проверка перехода по клику на лого Яндекса')
    @allure.step('Клик на лого Яндекс')
    def test_click_to_logo_ya(self, driver):
        driver.get(UrlPage.SAMOKAT_URL)
        main_page = MainPage(driver)
        main_page.click_to_logo(GoingPageLocators.LOGO_BUTTON_YA)
        driver.switch_to.window(driver.window_handles[-1])
        button_find = WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(GoingPageLocators.DZEN_BUTTON_FIND))
        assert button_find.is_displayed()

    @allure.title('Проверка перехода по клику на лого Самоката')
    @allure.step('Клик на лого Самокат')
    def test_click_to_logo_samokat(self, driver):
        driver.get(UrlPage.SAMOKAT_URL)
        main_page = MainPage(driver)
        main_page.click_button_order(OrderPageLocators.BUTTON_ORDER_MINI)
        main_page.click_to_logo(GoingPageLocators.LOGO_BUTTON_SAMOKAT)
        current_url = driver.current_url
        assert current_url == UrlPage.SAMOKAT_URL

