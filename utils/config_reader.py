from dotenv import load_dotenv
import os

load_dotenv()

class Config:

    BASE_URL = os.getenv("APP_BASE_URL")
    USERNAME = os.getenv("APP_USERNAME")
    PASSWORD = os.getenv("APP_PASSWORD")