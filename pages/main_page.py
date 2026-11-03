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

    @allure.step('клик по первому вопросу в разделе вопросы о важном ')
    def click_first_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.first_question)).click()

    @allure.step('возвращаем первый ответ на вопрос в разделе вопросы о важном ')
    def check_first_answer(self):
        element_first = self.wait.until(EC.visibility_of_element_located(self.locators.first_answer)).text
        return element_first

    @allure.step('клик по второму вопросу в разделе вопросы о важном ')
    def click_second_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.second_question)).click()

    @allure.step('возвращаем второй ответ на вопрос в разделе вопросы о важном ')
    def check_second_answer(self):
        element_second = self.wait.until(EC.visibility_of_element_located(self.locators.second_answer)).text
        return element_second

    @allure.step('клик по третьему вопросу в разделе вопросы о важном ')
    def click_third_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.third_question)).click()

    @allure.step('возвращаем третий ответ на вопрос в разделе вопросы о важном ')
    def check_third_answer(self):
        element_third = self.wait.until(EC.visibility_of_element_located(self.locators.third_answer)).text
        return element_third

    @allure.step('клик по четвертому вопросу в разделе вопросы о важном ')
    def click_fourth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.fourth_question)).click()

    @allure.step('возвращаем четвертый ответ на вопрос в разделе вопросы о важном ')
    def check_fourth_answer(self):
        element_fourth = self.wait.until(EC.visibility_of_element_located(self.locators.fourth_answer)).text
        return element_fourth

    @allure.step('клик по пятому вопросу в разделе вопросы о важном ')
    def click_fifth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.fifth_question)).click()

    @allure.step('возвращаем пятый ответ на вопрос в разделе вопросы о важном ')
    def check_fifth_answer(self):
        element_fifth = self.wait.until(EC.visibility_of_element_located(self.locators.fifth_answer)).text
        return element_fifth

    @allure.step('клик по шестому вопросу в разделе вопросы о важном ')
    def click_sixth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.sixth_question)).click()

    @allure.step('возвращаем шестой ответ на вопрос в разделе вопросы о важном ')
    def check_sixth_answer(self):
        element_sixth = self.wait.until(EC.visibility_of_element_located(self.locators.sixth_answer)).text
        return element_sixth

    @allure.step('клик по седьмому вопросу в разделе вопросы о важном ')
    def click_seven_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.seven_question)).click()

    @allure.step('возвращаем седьмой ответ на вопрос в разделе вопросы о важном ')
    def check_seven_answer(self):
        element_seven = self.wait.until(EC.visibility_of_element_located(self.locators.seven_answer)).text
        return element_seven

    @allure.step('клик по восьмому вопросу в разделе вопросы о важном ')
    def click_eighth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.eighth_question)).click()

    @allure.step('возвращаем восьмой ответ на вопрос в разделе вопросы о важном ')
    def check_eighth_answer(self):
        element_eighth = self.wait.until(EC.visibility_of_element_located(self.locators.eighth_answer)).text
        return element_eighth