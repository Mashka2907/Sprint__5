from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_page_locators import RegistrationPageLocators
from src.data import UserData
from faker import Faker


class TestRegistration:
    """Тесты для проверки функциональности регистрации пользователя."""

    def test_successful_registration(self, driver):
        fake = Faker("en_US")

        """1.Успешная регистрация пользователя."""
        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.no_account_button)).click()

        # 3. Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(fake.email())
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.confirm_password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.create_account_button)).click()

        # 4. Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.user_avatar)).is_displayed()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.user_name)).text == "User."

    def test_registration_with_invalid_email(self, driver):
        """2.Регистрация пользователя c email не по маске."""
        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.no_account_button)).click()

        # 3. Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(UserData.not_correct_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.confirm_password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.create_account_button)).click()

        # 4. Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        email_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field_error))
        password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field_error))
        confirm_password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.confirm_password_field_error))

        # Можно ли проверить, что поле выделено красным так assert "Error" in email_error.get_attribute("class") ?
        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert driver.find_element(*RegistrationPageLocators.email_error_message).text == "Ошибка"


    def test_register_an_existing_user(self, driver):
        """3.Регистрация существующего пользователя"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.no_account_button)).click()

        # 3. Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(UserData.correct_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.confirm_password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.create_account_button)).click()

        #4. Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        email_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field_error))
        password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field_error))
        confirm_password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.confirm_password_field_error))

        # Можно ли проверить, что поле выделено красным так assert "Error" in email_error.get_attribute("class") ?
        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert driver.find_element(*RegistrationPageLocators.email_error_message).text == "Ошибка"


    def test_user_login(self, driver):
        """4.Login пользователя"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать кнопку «Войти».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(UserData.correct_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_button)).click()

        # 3. Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.user_avatar)).is_displayed()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.user_name)).text == "User."


    def test_user_logout(self, driver):
        """5. Logout пользователя"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать кнопку «Войти».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(UserData.correct_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_button)).click()

        # 3. Нажать кнопку «Выйти».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.logout_button)).click()

        # 4. Проверить, что в правом верхнем углу около кнопки «Разместить объявление», теперь отображается кнопка «Вход и регистрация».
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).text == "Вход и регистрация"


    def test_ad_creation_by_unauthorized_user(self, driver):
        """6.Создание объявления неавторизованным пользователе"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Разместить объявление».
        driver.find_element(*RegistrationPageLocators.post_an_ad_button).click()

        # 2. Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.modal_window_with_message)).text == "Чтобы разместить объявление, авторизуйтесь"
    #

    def test_creation_of_an_ad_by_an_authorized_user(self, driver):
        """7.Создание объявления авторизованным пользователем"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_registration_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать кнопку «Войти».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.email_field)).send_keys(UserData.correct_email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.password_field)).send_keys(UserData.password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.login_button)).click()

        # 3. Нажать кнопку «Разместить объявление».
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.user_avatar))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationPageLocators.post_an_ad_button)).click()

        # 4. Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.product_name)).send_keys(UserData.name_product)
        driver.find_element(*RegistrationPageLocators.product_description).send_keys(UserData.description)
        driver.find_element(*RegistrationPageLocators.product_price).send_keys(UserData.price)

        # 5. Выбрать из Dropdown «Категорию» и «Город».
        driver.find_element(*RegistrationPageLocators.dropdown_categories).click()
        driver.find_element(*RegistrationPageLocators.select_categories).click()
        driver.find_element(*RegistrationPageLocators.dropdown_city).click()
        driver.find_element(*RegistrationPageLocators.select_city).click()

        # 6. Выбрать RabioButton «Состояние товара».
        driver.find_element(*RegistrationPageLocators.product_status).click()

        # 7. Нажать кнопку «Опубликовать».
        driver.find_element(*RegistrationPageLocators.publish_button).click()

        # 8. Скролл вверх и переход в профиль пользователя.
        driver.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.home_page))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationPageLocators.user_avatar)).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.name_product_home)).text == UserData.name_product











