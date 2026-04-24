from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=4)

def analyze(text):
    time.sleep(0.5)  # Simula carga de CPU
    if "hola" in text.lower():
        return "saludo"
    if "precio" in text.lower():
        return "consulta_precio"
    return "desconocido"

@app.route("/nlu", methods=["POST"])
def nlu():
    data = request.json
    future = executor.submit(analyze, data["text"])
    intent = future.result()
    return jsonify({"intent": intent})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
