from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_page_locators import RegistrationPageLocators
from data import UserData


class TestCreateAd:
    def test_ad_creation_by_unauthorized_user(self, driver):
        """6.Создание объявления неавторизованным пользователе"""

        driver.get(RegistrationPageLocators.main_page_url)

        # 1. Нажать кнопку «Разместить объявление».
        driver.find_element(*RegistrationPageLocators.post_an_ad_button).click()

        # 2. Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.modal_window_with_message)).text == "Чтобы разместить объявление, авторизуйтесь"


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

