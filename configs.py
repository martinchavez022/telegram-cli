import os
from dotenv import load_dotenv

class LoadConfigs:
    def __init__(self):
        load_dotenv()
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
