import pytest
from pages.main_page import MainPage
from pages.personal_data_page import PersonalDataPage

@pytest.mark.usefixtures("driver")
class TestLogo:
    def test_logo_scooter(self,driver):
        main_page = MainPage(driver)
        data_page = PersonalDataPage(driver)
        main_page.open()
        main_page.click_cookies_button()
        main_page.click_button_order()
        data_page.click_logo_scooter()
        assert data_page.check_click_logo_scooter() == 'https://qa-scooter.praktikum-services.ru/'

    def test_logo_yandex(self,driver):
        main_page = MainPage(driver)
        data_page = PersonalDataPage(driver)
        main_page.open()
        main_page.click_cookies_button()
        main_page.click_button_order()
        data_page.click_logo_yandex()
        assert 'dzen.ru' in data_page.check_click_logo_yandex()