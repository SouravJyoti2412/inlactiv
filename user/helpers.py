import requests
import random 
from base.settings import MESSEGE_API_KEY
def send_otp_ro_phone(phone_number):
    try:
        otp = random.randint(1000 ,9999)
        url = f"https://2factor.in/API/V1/{MESSEGE_API_KEY}/SMS/{phone_number}/{otp}"
        response = requests.get(url)
        return otp
    except Exception  as e:
        return None