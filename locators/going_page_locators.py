from selenium.webdriver.common.by import By


class GoingPageLocators:

    LOGO_BUTTON_YA = By.XPATH, '//a[@href = "//yandex.ru"]'
    LOGO_BUTTON_SAMOKAT = By.XPATH, '//a[@href= "/"]'
    DZEN_BUTTON_FIND = By.XPATH, '//button[text()="Найти"]'