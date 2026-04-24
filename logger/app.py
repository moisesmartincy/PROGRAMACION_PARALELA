from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    print(f"[{datetime.datetime.now()}] {data}")
    return {"status": "logged"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
