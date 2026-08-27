from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.CSS_SELECTOR, "a[href='/account']"
    LOGIN_PROFILE_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    MAIN_LIST_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_INGREDIENT = (By.CLASS_NAME, "BurgerIngredient_ingredient__text__yp3dH")
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Детали ингредиента
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  # закрытие всплывающего окна
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")  # Счетчик
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'  # Ваш заказ начали готовить в попапе
    ELEM_MODAL_WINDOW = (By.CSS_SELECTOR, 'div[class^="Modal_modal_overlay__"]')
    MODAL_OVERLAY = (By.CSS_SELECTOR, 'div[class*="Modal_modal_overlay"]')
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    MAIN_ORDER_H1 = By.XPATH, ".//p[text()='Соберите бургер']"


class AuthLoginLocators:
    # /login
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON_ANY_FORMS = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')    #ссылка "Восстановить пароль"
    LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    # LOGIN_TEXT_WITH_HREF = (By.XPATH, ".//a[text()='Войти']")  # Надпись Войти с ссылкой
    # LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")


class AuthForgotPasswordlocators:
    # /forgot-password
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить"

    # /reset-password
    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # поле пароль активно
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'  # кнопка "Показать пароль"
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить"

class UserProfileLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # Кнопка "История заказов"
    ENABLED_ORDER_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')  # Включенная кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LK_INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'персональные данные')]")


class OrdersPageLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]') # Заголовок "Лента заказов"
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ALL_ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    ALL_ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")

    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS_2 = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                         "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")