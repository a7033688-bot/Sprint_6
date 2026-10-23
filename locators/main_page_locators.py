from selenium.webdriver.common.by import By

class Main():

    order_button_in_header = (By.XPATH,".//button[@class='Button_Button__ra12g']")
    cookie_button =(By.XPATH,".//button[@id='rcc-confirm-button']")
    bottom_order_button = [By.XPATH,".//button[contains(@class,'1CSJM') and normalize-space()='Заказать']"]
    questions_about_important = [By.XPATH,".//div[@class='accordion']"]
    first_question = (By.XPATH,".//div[@id='accordion__heading-0']")
    first_answer = (By.XPATH,".//div[@id='accordion__panel-0']//p")
    second_question = (By.XPATH,".//div[@id='accordion__heading-1']")
    second_answer = (By.XPATH,".//div[@id='accordion__panel-1']//p")
    third_question = (By.XPATH,".//div[@id='accordion__heading-2']")
    third_answer = (By.XPATH,".//div[@id='accordion__panel-2']//p")
    fourth_question = (By.XPATH,".//div[@id='accordion__heading-3']")
    fourth_answer = (By.XPATH,".//div[@id='accordion__panel-3']//p")
    fifth_question = (By.XPATH,".//div[@id='accordion__heading-4']")
    fifth_answer = (By.XPATH,".//div[@id='accordion__panel-4']//p")
    sixth_question =(By.XPATH,".//div[@id='accordion__heading-5']")
    sixth_answer = (By.XPATH,".//div[@id='accordion__panel-5']//p")
    seven_question = (By.XPATH,".//div[@id='accordion__heading-6']")
    seven_answer = (By.XPATH,".//div[@id='accordion__panel-6']//p")
    eighth_question = (By.XPATH,".//div[@id='accordion__heading-7']")
    eighth_answer = (By.XPATH,".//div[@id='accordion__panel-7']//p")
