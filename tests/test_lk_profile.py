import allure
from urls import Urls
from pages.main_page import MainPage
from pages.user_profile_page import UserProfilePage
from pages.auth_user_page import AuthUserPage


class TestLKProfile:
    @allure.title('Переход в ЛК по клику на "Личный кабинет"')
    @allure.description('При нажатии на кнопку ЛК, происходит переход на страницу ЛК профиля')
    def test_go_to_account_from_header(self, driver, create_user):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])
        main_page = MainPage(driver)

        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        current_url = user_profile_page.check_switch_on_profile()
        assert current_url == Urls.url_profile

    @allure.title('Переход в ЛК в раздел История заказов по кнопке "История заказов"')
    @allure.description('При нажатии на кнопку "История заказов" в ЛК профиля, происходит переход к истории заказов юзера')
    def test_go_to_order_history(self, driver, create_user):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])
        main_page = MainPage(driver)

        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_order_history_button()
        current_url = user_profile_page.check_switch_on_order_history()
        assert current_url == Urls.url_profile_order_history

    @allure.title('Переход на страницу авторизации при нажатии в ЛК кнопки "Выход"')
    @allure.description('При нажатии в ЛК профиля кнопки "Выход" происходит разлогин пользователя на сайте и редирект на страницу авторизации')
    def test_logout(self, driver, create_user):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])
        main_page = MainPage(driver)
        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_log_out_button()
        current_url = auth_user_page.check_switch_on_login_page()
        assert current_url == Urls.url_login