from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
IP_RANGE = os.getenv("IP_RANGE")
