import requests
import time 

from configs import LoadConfigs

cf = LoadConfigs()
URL = f"https://api.telegram.org/bot{cf.BOT_TOKEN}/getUpdates"

def get_chat_id():
    last_update_id = None
    print("ENvia un mensaje a tu bot en Telegram....")

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
                    return chat_id
        except Exception as e:
            print("Error:", e)

        time.sleep(2)

if __name__ == "__main__":
    get_chat_id()

