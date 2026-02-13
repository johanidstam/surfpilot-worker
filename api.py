from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

DATA_FILE = "data.json"


@app.route("/")
def home():
    return "API is running"


@app.route("/data")
def data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"plans": []})

    with open(DATA_FILE) as f:
        return jsonify(json.load(f))


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))

    app.run(host="0.0.0.0", port=port)

