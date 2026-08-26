import pytest
import requests
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from urls import Urls
from helpers import User

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def create_user():
    payload = User.generate_user()
    response = requests.post(f"{User.BASE_URL}/api/auth/register", data=payload)
    if response.status_code == 200:
        token = response.json().get('accessToken')
        yield payload, token
        headers = {"Authorization": token}
        requests.delete(f"{User.BASE_URL}/api/auth/user", headers=headers)
    else:
        pytest.fail(f'Не удалось создать пользователя через API'
                    f'Статус: {response.status_code}, Ответ: {response.text}')

