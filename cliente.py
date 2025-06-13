import requests
import time

URL = "https://control-remoto.onrender.com/comando"

while True:
    try:
        data = {"comando": "whoami"}
        r = requests.post(URL, json=data, timeout=10)
        print("[+] Respuesta:", r.json())
    except Exception as e:
        print("[!] Error al obtener comando:", e)
    time.sleep(5)
