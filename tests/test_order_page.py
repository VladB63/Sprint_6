import allure
import pytest
from data import OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators



class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
        "locator, order_data", [
            (OrderPageLocators.BUTTON_ORDER_MINI, OrderData.DATA_ORDER_1),
            (OrderPageLocators.BUTTON_ORDER_BIG, OrderData.DATA_ORDER_2)
        ]
    )
    def test_making_order_button(self, driver, locator, order_data):
        main_page = MainPage(driver)
        main_page.open_url_samokat()
        main_page.click_button_order(locator)
        order_page = OrderPage(driver)
        order_page.completion_fields(order_data)
        modal_complit = order_page.find_modal_window()
        assert modal_complit.is_displayed()






