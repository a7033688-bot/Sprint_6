import pytest
from pages.main_page import MainPage
from pages.personal_data_page import PersonalDataPage

@pytest.mark.usefixtures("driver")
class TestCheckEntryPointsIntoScript:
   
    @pytest.mark.parametrize('names, surnames, house, numbers, value', 
                            [['Андрей', 'Иванов', 'улица Ленина', '89999999999', 'Лубянка'], 
                             ['Алена', 'Петрова', 'улица Пушкина', '87777777777', 'Спортивная']])
    def test_order_scooter(self,driver,names,surnames,house,numbers,value):
        main_page = MainPage(driver)
        data_page = PersonalDataPage(driver)
        main_page.open()
        main_page.click_cookies_button()
        main_page.click_button_order() 
        data_page.fill_all_fields(names, surnames, house, numbers, value)
        data_page.click_next_button()
        data_page.order()
        assert data_page.check_url_track() == True

    def test_mark_second_entry_point_in_scenario(self,driver):
        main_page = MainPage(driver)
        data_page = PersonalDataPage(driver)
        main_page.open()
        main_page.click_cookies_button()
        main_page.scroll_botton_order_button()
        assert data_page.check_check_url_order() == True