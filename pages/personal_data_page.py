import time
from locators.personal_data_page_locators import Placeholdor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PersonalDataPage():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Placeholdor
        self.wait= WebDriverWait(driver,10)

    def fill_all_fields(self,names,surnames,house,numbers,value):
        self.driver.find_element(*self.locators.name).send_keys(names)
        self.driver.find_element(*self.locators.surname).send_keys(surnames)
        self.driver.find_element(*self.locators.addres).send_keys(house)
        self.wait.until(EC.element_to_be_clickable(self.locators.metro)).send_keys(value)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.locators.metro_list)).click()
        self.wait.until(EC.element_to_be_clickable(self.locators.number)).send_keys(numbers)

    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.next_button)).click()
        

    def date_selection(self):
    
        self.driver.find_element(*self.locators.when_bring).click()
        self.wait.until(EC.element_to_be_clickable(self.locators.today_date)).click()

    def choosing_rental_period(self):
        self.driver.find_element(*self.locators.rental_period).click()
        self.driver.find_element(*self.locators.one_day).click()

    def choosing_color_scooter(self):
        self.driver.find_element(*self.locators.black_scooter).click()

    def button_order(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.order_button)).click()

    def positive_confirmation_button(self):
        self.driver.find_element(*self.locators.positive_confirmation_button).click()

    def status_button(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.locators.status_button)).click()

    def order(self):
        self.date_selection()
        self.choosing_rental_period()
        self.choosing_color_scooter()
        self.button_order()
        self.positive_confirmation_button()
        self.status_button()
            

    def check_check_url_order(self):
            current_url = self.driver.current_url
            return 'https://qa-scooter.praktikum-services.ru/order' in current_url

    def check_url_track(self):
            current_url = self.driver.current_url
            return 'https://qa-scooter.praktikum-services.ru/track' in current_url
    
    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.logo_yandex)).click()

    def check_click_logo_yandex(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_contains('dzen.ru'))
        return self.driver.current_url

    def click_logo_scooter(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.logo_scooter)).click()
    
    def check_click_logo_scooter(self):
        current_url = self.driver.current_url
        return current_url 
        
        
        
