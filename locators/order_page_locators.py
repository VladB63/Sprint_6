from selenium.webdriver.common.by import By

class OrderPageLocators:

    BUTTON_ORDER_MINI = By.CLASS_NAME, 'Button_Button__ra12g'  # кнопка заказать вверху страницы
    BUTTON_ORDER_BIG = By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp'  # кнопка заказать внизу страницы
    METRO_STATION = By.XPATH, '//input[@placeholder="* Станция метро"]'  # поле станции метро
    BUTTON_ORDER_NEXT = By.XPATH, '//button[text()= "Далее"]'  # кнопка далее на странице ввода фио
    NAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'  # поле ввода имени
    FIRST_NAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'  # поле ввода фамилии
    ADDRESS_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'  # поле ввода адреса
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'  # поле ввода номера телефона
    DATA_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  # поле выбора даты привоза
    CALENDAR = By.XPATH, '//*[text()="30"]'  # выбор самой даты привоза
    TERM_FIELD = By.CLASS_NAME, 'Dropdown-placeholder'  # выпадающий список выбора срока аренды
    DROPDOWN_DAYS = By.XPATH, '//*[text()="сутки"]'  # выбор срока аренды из выпадающего списка
    GREY_CHECKBOX = By.ID, 'grey'  # чек бокс выбора цвета
    BLACK_CHECKBOX = By.ID, 'black'  # чек бокс выбора цвета
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'  # поле ввода комментария
    BUTTON_COMPLIT = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'  # кнопка заказать после ввода всех данных
    BUTTON_YES = By.XPATH, '//button[text()="Да"]'  # кнопка подтверждения оформления заказа
    MODAL_WINDOW = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'  # модальное окно об успешном оформлении

    NAME_STATION = By.XPATH, "//*[text()='{}']"

