import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """
        Добавляет опцию командной строки для выбора браузера, который будет использоваться для выполнения тестов.

        :param parser: объект парсера командной строки pytest
        :return: None
        """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


# Функция для инициализации веб-драйвера
def initialize_driver(browser_name):
    # Определение опций в зависимости от выбранного браузера
    options = (ChromeOptions() if browser_name == "chrome" else FirefoxOptions() if browser_name == "firefox" else None)
    if options is None:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    # Настройка опций для запуска в CI-среде
    if 'CI' in os.environ:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--remote-debugging-pipe')  # экспериментальный параметр для отладки
        options.add_argument('window-size=1920,1080')
        driver = getattr(webdriver, browser_name.capitalize())(options=options)

    # Максимизация окна браузера (не применяется в CI-среде)
    elif 'CI' not in os.environ:
        options.add_argument('--headless')  # для отладки
        # driver = getattr(webdriver, browser_name.capitalize())(options=options)
        # driver.maximize_window()

    return driver


# Фикстура для инициализации веб-драйвера
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    try:
        print("\nstart browser...")
        # Получение имени браузера из параметров командной строки
        browser_name = request.config.getoption("browser_name").lower()
        # Инициализация веб=драйвера
        driver = initialize_driver(browser_name)
        # Привязка объекта веб-драйвера к аттрибуту класса для использования в тестах
        request.cls.driver = driver
        # Возврат объекта веб-драйвера для использования в тестах
        yield driver
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("\nquit browser...")
        # Завершение работы веб-драйвера после завершения тестов
        if driver:
            driver.quit()
