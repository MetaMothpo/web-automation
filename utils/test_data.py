import random
import string

def generate_random_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@gmail.com"

def get_test_user_data():
    return {
        "first_name": "meta",
        "last_name": "mothapo",
        "dob": "1990-01-01",
        "address": "123 Test Street",
        "postcode": "12345",
        "city": "Test City",
        "state": "Test State",
        "country": "ZA",
        "phone": "1234567890",
        "email": "meta@gmail.com",
        "password": "Test@123"
    } 