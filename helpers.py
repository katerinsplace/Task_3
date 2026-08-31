import random
import string

class User:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    
    @staticmethod
    def generate_user():
        name = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = name + '@yandex.ru'
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        
        return {"email": email, "password": password, "name": name}
