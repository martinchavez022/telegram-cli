import requests
import time
from db import DatabaseActivity as DBAc

from configs import LoadConfigs

db_conn = DBAc()

# base de datos para almacenar las variables del chat

cf = LoadConfigs()
URL = f"https://api.telegram.org/bot{cf.BOT_TOKEN}/getUpdates"

def get_chat_id():
    last_update_id = None
    print("Envia un mensaje al chat con el bot..")

    while True:
        try:
            res = requests.get(URL, params={"offset": last_update_id})
            data = res.json()

            if "result" in data and len(data["result"]) > 0:
                for update in data["result"]:
                    last_update_id = update["update_id"] + 1
                    chat_id = update["message"]["chat"]["id"]
                    user = update["message"]["from"]["first_name"]

                    print(f" chat_id encontrado: {chat_id} (usuario: {user})")
                    db_conn.insert_chat(chat_id, "Chat Bot"),
                    return chat_id
        except Exception as e:
            print("Error:", e)

        time.sleep(2)

if __name__ == "__main__":
    get_chat_id()

