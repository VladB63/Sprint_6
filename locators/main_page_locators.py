from selenium.webdriver.common.by import By


class MainPageLocators:

    PANEL_QUESTION = By.ID, 'accordion__heading-{}'  # панель с вопросом
    PANEL_ANSWER = By.ID, 'accordion__panel-{}'  # панель с ответом
    SCROLL_TO_QUESTION = By.ID, 'accordion__heading-7'  # скрол к последнему вопросу


