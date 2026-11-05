import allure
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    URL = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('открыть главную страницу самоката')
    def open(self):
        self.driver.get(self.URL)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_center(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])