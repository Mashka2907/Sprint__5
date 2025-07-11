import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия экземпляра драйвера Chrome."""
    chrome_options = ChromeOptions()
    # Добавьте опции, если необходимо (например, для headless-режима)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()