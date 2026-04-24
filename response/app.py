from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/response", methods=["POST"])
def response():
    intent = request.json["intent"]

    responses = {
        "saludo": "Hola, ¿en qué puedo ayudarte?",
        "consulta_precio": "El precio es 100 Bs.",
        "desconocido": "No entendí tu mensaje."
    }

    return jsonify({"response": responses.get(intent)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
