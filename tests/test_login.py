from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_page_locators import RegistrationPageLocators
from src.data import UserData


class TestLogin:
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