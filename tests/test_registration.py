from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_page_locators import RegistrationPageLocators
from data import UserData
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










