import redis
import pyautogui
import ast


# untuk membuat koneksi ke redis
conn = redis.Redis(host='localhost', port=6379, db=0)

p = conn.pubsub()
p.subscribe('TokoCabang')

while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        data = message['data'].decode('utf-8')
        value = ast.literal_eval(data)
        print(f"Title: {value[0]} Message: {value[1]}")
        pyautogui.alert(value[1], value[0])  # always returns "OK"
