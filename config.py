from dotenv import load_dotenv
from decouple import config

load_dotenv()

api_domain = config('API_DOMAIN', default='http://127.0.0.1:8000')
