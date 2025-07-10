from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """Локаторы для страницы регистрации."""

    # Кнопка "Вход и регистрация"
    login_registration_button = By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"

    # Кнопка "Разместить объявление"
    post_an_ad_button = By.XPATH, "//*[text()='Разместить объявление']"

    # Кнопка "Нет аккаунта"
    no_account_button = By.XPATH, "//button[text()='Нет аккаунта']"

    # Поле "Email"
    email_field = By.NAME, "email"

    # Поле "Пароль"
    password_field = By.NAME, "password"

    # Поле "Повторите пароль"
    confirm_password_field = By.NAME, "submitPassword"

    # Поле "Email" подсвечено красным
    email_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[1]"

    # Поле "Пароль" подсвечено красным
    password_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[2]"

    # Поле "Повторите пароль" подсвечено красным
    confirm_password_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[3]"

    # Кнопка "Войти"
    login_button = By.XPATH, "//button[text()='Войти']"

    # Кнопка "Выйти"
    logout_button = By.XPATH, "//button[text()='Выйти']"

    # Кнопка "Создать аккаунт"
    create_account_button = By.XPATH, "//button[text()='Создать аккаунт']"

    # Сообщение об ошибке под полем Email
    email_error_message = By.XPATH, "//span[text()='Ошибка']"

    # Модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»
    modal_window_with_message = By.XPATH, "//h1[@class='h1']"

    # Аватар пользователя (после успешной регистрации)
    user_avatar = By.XPATH, '//button[@class="circleSmall"]'

    # Имя пользователя (после успешной регистрации)
    user_name = By.XPATH, "//h3[@class='profileText name']"

    # Название товара
    product_name = By.XPATH, "//input[@name='name']"

    # Описание товара
    product_description = By.XPATH, "//textarea[@name='description']"

    # Стоимость товара
    product_price = By.XPATH, "//input[@name='price']"

    # Dropdown "Город"
    dropdown_city = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"

    # Выбор города (Казань)
    select_city = By.XPATH, "//span[text()='Казань']"

    # Dropdown "Категории"
    dropdown_categories = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]"

    # Выбор категории (Книги)
    select_categories = By.XPATH, "//span[text()='Книги']"

    # RabioButton "Состояние товара" Б/У
    product_status = By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular')]"

    # Кнопка "Опубликовать"
    publish_button = By.XPATH, "//button[text()='Опубликовать']"

    # Прогрузка профиля
    home_page = By.XPATH, "//*[contains(@class, 'homePage_homepage')]"

    # Название объявления в разделе "Мои объявления"
    name_product_home = By.XPATH, "//h2[text()='Преступление и наказание']"

    # Главная страница
    main_page_url = "https://qa-desk.stand.praktikum-services.ru/"