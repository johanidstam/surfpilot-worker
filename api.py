from flask import Flask, jsonify
import json
import os


app = Flask(__name__)


@app.route("/data")
def data():

    if not os.path.exists("data.json"):
        return jsonify({"plans": []})

    with open("data.json") as f:
        return jsonify(json.load(f))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
