import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:
    """
    для работы с конфиденциальными данными (логины и пароли)
    """
    login = os.getenv("qa_login")
    password = os.getenv("qa_password")