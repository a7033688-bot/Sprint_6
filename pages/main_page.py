import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import Main
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locators = Main

    @allure.step('Кликаем по кнопке принять куки если она есть')
    def click_cookies_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.locators.cookie_button)).click()
        except TimeoutException:
            pass

    @allure.step('Скролим до второй кнопки заказать и кликаем по ней')
    def scroll_botton_order_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.locators.bottom_order_button))
        self.scroll_to_center(element)
        element.click()    

    @allure.step('кликаем по кнопке заказать в шапке')
    def click_button_order(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.order_button_in_header)).click()

    @allure.step('скролим до футера')
    def scroll_footer(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.questions_about_important))
        self.scroll_to_element(element)

    def get_answer_text(self, question, answer):
        self.wait.until(EC.element_to_be_clickable(question)).click()
        return self.wait.until(EC.visibility_of_element_located(answer)).text