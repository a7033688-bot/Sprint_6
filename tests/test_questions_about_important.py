import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("driver")
class TestCheckEntryPointsIntoScript:

    def test_first_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_first_question()
        assert main_page.check_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_second_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_second_question()
        assert main_page.check_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_third_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_third_question()
        assert main_page.check_third_answer() == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_fourth_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_fourth_question()
        assert main_page.check_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_fifth_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_fifth_question()
        assert main_page.check_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_sixth_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_sixth_question()
        assert main_page.check_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_seven_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_seven_question()
        assert main_page.check_seven_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_eighth_question(self,driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        main_page.click_eighth_question()
        assert main_page.check_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'