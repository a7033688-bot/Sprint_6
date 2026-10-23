from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import Main


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = Main
        self.wait= WebDriverWait(driver,10)

    def open(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def click_cookies_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.locators.cookie_button)).click()
        except TimeoutException:
            pass

    def scroll_botton_order_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.locators.bottom_order_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()    
    
    def click_button_order(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.order_button_in_header)).click()

    def scroll_footer(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.questions_about_important))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_first_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.first_question)).click()

    def check_first_answer(self):
        element_first = self.wait.until(EC.presence_of_element_located(self.locators.first_answer)).text
        return element_first

    def click_second_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.second_question)).click()
    
    def check_second_answer(self):
        element_second = self.wait.until(EC.presence_of_element_located(self.locators.second_answer)).text
        return element_second

    def click_third_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.third_question)).click()
        
    def check_third_answer(self):
        element_third = self.wait.until(EC.presence_of_element_located(self.locators.third_answer)).text
        return element_third

    def click_fourth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.fourth_question)).click()
            
    def check_fourth_answer(self):
        element_fourth = self.wait.until(EC.presence_of_element_located(self.locators.fourth_answer)).text
        return element_fourth

    def click_fifth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.fifth_question)).click()
                
    def check_fifth_answer(self):
        element_fifth = self.wait.until(EC.presence_of_element_located(self.locators.fifth_answer)).text
        return element_fifth

    def click_sixth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.sixth_question)).click()
                    
    def check_sixth_answer(self):
        element_sixth = self.wait.until(EC.presence_of_element_located(self.locators.sixth_answer)).text
        return element_sixth

    def click_seven_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.seven_question)).click()
                        
    def check_seven_answer(self):
        element_seven = self.wait.until(EC.presence_of_element_located(self.locators.seven_answer)).text
        return element_seven

    def click_eighth_question(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.eighth_question)).click()
                            
    def check_eighth_answer(self):
        element_eighth = self.wait.until(EC.presence_of_element_located(self.locators.eighth_answer)).text
        return element_eighth