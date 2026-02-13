from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/data.json"


@app.route("/data")
def data():

    if not os.path.exists(DATA_FILE):
        return jsonify({"plans": []})

    try:
        with open(DATA_FILE) as f:
            return jsonify(json.load(f))

    except Exception as e:

        print("Read error:", e)

        return jsonify({
            "plans": [],
            "error": "Temporary read error"
        })


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(host="0.0.0.0", port=port)
