from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNaME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DATABASE = os.getenv("DATABASE")
DB_PORT = os.getenv("PORT")