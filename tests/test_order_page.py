import allure
import pytest
from data import UrlPage, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators



class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @allure.step('Оформление заказа')
    @pytest.mark.parametrize(
        "locator, order_data", [
            (OrderPageLocators.BUTTON_ORDER_MINI, OrderData.DATA_ORDER_1),
            (OrderPageLocators.BUTTON_ORDER_BIG, OrderData.DATA_ORDER_2)
        ]
    )
    def test_making_order_button(self, driver, locator, order_data):
        driver.get(UrlPage.SAMOKAT_URL)
        main_page = MainPage(driver)
        main_page.click_button_order(OrderPageLocators.BUTTON_ORDER_MINI)
        order_page = OrderPage(driver)
        order_page.completion_fields(order_data)
        modal_complit = order_page.find_element_with_wait(OrderPageLocators.MODAL_WINDOW)
        assert modal_complit.is_displayed()






