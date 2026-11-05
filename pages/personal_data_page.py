import allure
import time
from locators.personal_data_page_locators import Placeholdor
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PersonalDataPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Placeholdor

    @allure.step('вводим персональные данные')
    def fill_all_fields(self,names,surnames,house,numbers,value):
        self.find(self.locators.name).send_keys(names)
        self.find(self.locators.surname).send_keys(surnames)
        self.find(self.locators.addres).send_keys(house)
        element = self.find(self.locators.metro)
        element.click()
        element.send_keys(value[:4])
        self.wait.until(EC.presence_of_element_located((self.locators.one_metro)))
        station =(By.XPATH, self.locators.metro_list.format(value=value))
        self.wait.until(EC.visibility_of_element_located(station)).click()
        self.wait.until(EC.element_to_be_clickable(self.locators.number)).send_keys(numbers)

    @allure.step('клик по кнопке далее')
    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.next_button)).click()        

    @allure.step('нажимаем на поле выбора даты')
    def date_selection(self):    
        self.find(self.locators.when_bring).click()
        self.wait.until(EC.element_to_be_clickable(self.locators.today_date)).click()

    @allure.step('выбираем в календаре дату "сегодня" и срок аренды одни сутки')
    def choosing_rental_period(self):
        self.find(self.locators.rental_period).click()
        self.find(self.locators.one_day).click()

    @allure.step('выбираем цвет самоката ')
    def choosing_color_scooter(self):
        self.find(self.locators.black_scooter).click()

    @allure.step('нажимаем на кнопку заказать')
    def button_order(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.order_button)).click()

    @allure.step('в окне подтверждения нажимаем "Да"')
    def positive_confirmation_button(self):
        self.find(self.locators.positive_confirmation_button).click()

    @allure.step('нажимаем на кнопку "Посмотреть статус заказа"')
    def status_button(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.locators.status_button)).click()

    @allure.step('обеденяем в шаг методы для окна "Выбор самоката"')
    def order(self):
        self.date_selection()
        self.choosing_rental_period()
        self.choosing_color_scooter()
        self.button_order()
        self.positive_confirmation_button()
        self.status_button()
            
    @allure.step('проверка что мы находимся на странице заказа самоката')
    def check_check_url_order(self):
            current_url = self.get_current_url()
            return 'https://qa-scooter.praktikum-services.ru/order' in current_url

    @allure.step('проверка что мы находимся на странице статус заказа')
    def check_url_track(self):
            current_url = self.get_current_url()
            return 'https://qa-scooter.praktikum-services.ru/track' in current_url

    @allure.step('клик по логотипу Яндекс')
    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.logo_yandex)).click()

    @allure.step('проверка что после клика по логотипу Яндекса мы переходим на страницу Дзена')
    def check_click_logo_yandex(self):
        self.switch_to_last_tab()
        self.wait.until(EC.url_contains('dzen.ru'))
        return self.get_current_url()

    @allure.step('клик по логотипу самокат')
    def click_logo_scooter(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.logo_scooter)).click()

    @allure.step('проверка что после клика по логотипу самоката мы переходим на главную страницу самоката')
    def check_click_logo_scooter(self):
        return self.get_current_url()

        
        
        
