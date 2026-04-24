from flask import Flask, request, jsonify
import requests
from flask_cors import CORS   # 👈 NUEVO

app = Flask(__name__)
CORS(app)  # 👈 HABILITA CORS

NLU_URL = "http://nlu:5001/nlu"
RESP_URL = "http://response:5002/response"
LOG_URL = "http://logger:5003/log"

@app.route("/chat", methods=["POST"])
def chat():
    text = request.json["text"]

    intent = requests.post(NLU_URL, json={"text": text}).json()["intent"]
    reply = requests.post(RESP_URL, json={"intent": intent}).json()["response"]

    requests.post(LOG_URL, json={
        "text": text,
        "intent": intent,
        "response": reply
    })

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
