from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "API is running"


@app.route("/data")
def data():
    plans = [
        {"operator": "Hallon", "gb": 100, "price": 115},
        {"operator": "Vimla", "gb": 60, "price": 170},
        {"operator": "Comviq", "gb": 50, "price": 185},
        {"operator": "Fello", "gb": 50, "price": 265},
        {"operator": "Telenor", "gb": 100, "price": 279},
    ]

    return jsonify({"plans": plans})


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
