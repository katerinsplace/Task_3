import allure
from urls import Urls
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage



class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по клику на "Восстановить пароль" на странице логина')
    def test_click_password_reset_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_account()
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.click_password_reset_link()
        current_url = recovery_page.get_current_url()
        assert current_url == Urls.url_restore

    @allure.title('Ввод почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, driver, create_user):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_link(Urls.url_restore)
        recovery_page.set_email_for_reset_password(create_user[0]['email'])
        recovery_page.click_reset_button()
        recovery_page.find_save_button()
        current_url = recovery_page.get_current_url()
        assert current_url == Urls.url_reset

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, driver, create_user):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_link(Urls.url_restore)
        recovery_page.set_email_for_reset_password(create_user[0]['email'])
        recovery_page.click_reset_button()
        recovery_page.find_save_button()
        recovery_page.click_on_show_password_button()
        assert recovery_page.find_input_active()