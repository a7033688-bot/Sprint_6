from selenium.webdriver.common.by import By

class Placeholdor():
    name = [By.CSS_SELECTOR,'[placeholder="* Имя"]']
    surname = [By.CSS_SELECTOR,'[placeholder="* Фамилия"]']
    addres = [By.CSS_SELECTOR,'[placeholder="* Адрес: куда привезти заказ"]']
    metro = [By.CSS_SELECTOR,'[placeholder="* Станция метро"]']
    metro_list = [By.CLASS_NAME, 'select-search__select']
    number = [By.CSS_SELECTOR,'[placeholder="* Телефон: на него позвонит курьер"]']
    next_button = (By.XPATH, "./html/body/div/div/div/div/button[normalize-space()='Далее']")
    when_bring = [By.CSS_SELECTOR,'[placeholder="* Когда привезти самокат"]']
    today_date = [By.XPATH,".//div[contains(@class,'today')]"]
    rental_period = [By.CLASS_NAME,'Dropdown-placeholder']
    one_day = [By.XPATH,".//div[text()='сутки']"]
    black_scooter = [By.ID,'black']
    gray_scooter = [By.ID,'grey']
    order_button = [By.XPATH,".//button[contains(@class,'1CSJM') and normalize-space()='Заказать']"]
    positive_confirmation_button = [By.XPATH,".//button[contains(@class,'Button_Middle__1CSJM') and normalize-space()='Да']"]
    status_button = [By.XPATH,".//button[contains(@class,'1CSJM') and normalize-space()='Посмотреть статус']"]
    positive_confirmation =[By.CSS_SELECTOR,'.Order_Text__2broi']
    logo_yandex = [By.XPATH,".//img[@alt='Yandex']"]
    logo_scooter = [By.XPATH,".//img[@alt='Scooter']"]