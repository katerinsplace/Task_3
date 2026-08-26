import allure
import pytest

from locators import OrdersPageLocators
from pages.main_page import MainPage
from pages.create_order_page import CreateOrderPage
from pages.auth_user_page import AuthUserPage
from pages.user_profile_page import UserProfilePage
from pages.create_order_page import CreateOrderPage


class TestCreateOrder:
    @allure.title('Проверка появления всплывающего окна с деталями при клике на заказ')
    @allure.description('Кликаем на заказ и проверяем, что появилось всплывающее окно с деталями')
    def test_get_order_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_list_button()
        create_order_page = CreateOrderPage(driver)
        create_order_page.click_order()
        assert create_order_page.check_order_structure() == True

    @allure.title('При создании заказа он отображается как и в Истории заказов в ЛК профиля, так и в "Ленте заказов"')
    @allure.description('Создаем заказ и проверяем, есть ли он в ЛК в Истории заказов, и есть ли этот же заказ в "Ленте заказов"')
    def test_find_order_in_list(self, driver, create_user):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])

        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.check_show_window_with_order_id()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_on_account()

        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_order_history_button()

        create_order = CreateOrderPage(driver)
        is_order_id_found_at_history = create_order.is_order_id_found_at_history(order_number)

        main_page.click_orders_list_button()
        is_order_id_found_at_feed = create_order.is_order_id_found_at_feed(order_number)
        assert is_order_id_found_at_history and is_order_id_found_at_feed

    @allure.title('При создании заказа, происходит увеличение значения счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')
    @allure.description('Сверяем счетчик заказов "Выполнено за все время" / "Выполнено за сегодня" до создания заказа и после создания заказа'
                        'Счетчик должен увеличиться')
    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT, OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, driver, create_user, counter):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])

        main_page = MainPage(driver)
        main_page.click_orders_list_button()

        create_order = CreateOrderPage(driver)
        prev_counter_value = create_order.get_total_order_count_daily(counter)

        main_page.click_constructor_button()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.click_close_modal_order()
        main_page.click_orders_list_button()

        current_counter_value = create_order.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"

    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_new_order_appears_in_work_list(self, driver, create_user):
        auth_user_page = AuthUserPage(driver)
        auth_user_page.login(create_user[0])

        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list_button()

        create_order = CreateOrderPage(driver)
        order_number_refactor = create_order.get_user_order(order_number)
        order_in_progress = create_order.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress