import allure 
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import Main 


QUESTIONS = [
    (Main.first_question, Main.first_answer,
     'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (Main.second_question, Main.second_answer,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (Main.third_question, Main.third_answer,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (Main.fourth_question, Main.fourth_answer,
     'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (Main.fifth_question, Main.fifth_answer,
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (Main.sixth_question, Main.sixth_answer,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (Main.seven_question, Main.seven_answer,
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (Main.eighth_question, Main.eighth_answer,
     'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
]

@pytest.mark.usefixtures("driver")
class TestCheckEntryPointsIntoScript:

    @pytest.mark.parametrize('question, answer, expected', QUESTIONS)
    @allure.title('Проверка ответа на вопрос в разделе «Вопросы о важном»')
    def test_question(self, driver, question, answer, expected):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_footer()
        assert main_page.get_answer_text(question, answer) == expected 
    
    