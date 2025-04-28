import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):


    @allure.step('Оформление заказа')
    def completion_fields(self, data):

        self.add_text_to_element(OrderPageLocators.NAME_FIELD, data["name"])
        self.add_text_to_element(OrderPageLocators.FIRST_NAME_FIELD, data["first_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION)
        locator_format = self.format_locators(OrderPageLocators.NAME_STATION, data['station'])
        self.click_to_element(locator_format)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, data["phone"])
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_NEXT)
        self.find_element_with_wait(OrderPageLocators.DATA_FIELD)
        self.click_to_element(OrderPageLocators.DATA_FIELD)
        self.click_to_element(OrderPageLocators.CALENDAR)
        self.click_to_element(OrderPageLocators.TERM_FIELD)
        self.click_to_element(OrderPageLocators.DROPDOWN_DAYS)
        self.click_to_element(OrderPageLocators.GREY_CHECKBOX)
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, data["comment"])
        self.click_to_element(OrderPageLocators.BUTTON_COMPLIT)
        self.click_to_element(OrderPageLocators.BUTTON_YES)





