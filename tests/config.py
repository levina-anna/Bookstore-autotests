from dotenv import load_dotenv
from decouple import config

load_dotenv()

domain = config('DOMAIN', default='http://127.0.0.1:8000')
