from selenium.webdriver.common.by import By

class Main():

    order_button_in_header = [By.XPATH,".//div[@class='Header_Nav__AGCXC']//button[normalize-space()='Заказать']"]
    cookie_button =(By.XPATH,".//button[@id='rcc-confirm-button']")
    bottom_order_button = [By.XPATH,".//div[@class='Home_FinishButton__1_cWm']//button"]
    questions_about_important = [By.XPATH,".//div[@class='accordion']"]
    first_question = (By.XPATH,".//div[normalize-space()='Сколько это стоит? И как оплатить?']")
    first_answer = (By.XPATH,".//div[normalize-space()='Сколько это стоит? И как оплатить?']/parent::div/following-sibling::div/p")
    second_question = (By.XPATH, ".//div[starts-with(text(),'Хочу сразу несколько самокатов!')]")
    second_answer = (By.XPATH,".//div[starts-with(text(),'Хочу сразу несколько самокатов!')]/parent::div/following-sibling::div/p")
    third_question = (By.XPATH, ".//div[starts-with(text(),'Как рассчитывается')]")
    third_answer = (By.XPATH,".//div[starts-with(text(),'Как рассчитывается')]/parent::div/following-sibling::div/p")
    fourth_question = (By.XPATH, ".//div[starts-with(text(),'Можно ли заказать')]")
    fourth_answer = (By.XPATH,".//div[starts-with(text(),'Можно ли заказать')]/parent::div/following-sibling::div/p")
    fifth_question = (By.XPATH, ".//div[starts-with(text(),'Можно ли продлить заказ')]")
    fifth_answer = (By.XPATH,".//div[starts-with(text(),'Можно ли продлить заказ')]/parent::div/following-sibling::div/p")
    sixth_question =(By.XPATH, ".//div[starts-with(text(),'Вы привозите зарядку')]")
    sixth_answer = (By.XPATH,".//div[starts-with(text(),'Вы привозите зарядку')]/parent::div/following-sibling::div/p")
    seven_question = (By.XPATH, ".//div[starts-with(text(),'Можно ли отменить')]")
    seven_answer = (By.XPATH,".//div[starts-with(text(),'Можно ли отменить')]/parent::div/following-sibling::div/p")
    eighth_question = (By.XPATH, ".//div[starts-with(text(),'Я жизу за МКАДом')]")
    eighth_answer = (By.XPATH,".//div[starts-with(text(),'Я жизу за МКАДом')]/parent::div/following-sibling::div/p")
