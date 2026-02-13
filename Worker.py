import requests
import json
import time


URL = "https://www.hallon.se/mobilabonnemang"


def fetch_data():
    r = requests.get(URL, timeout=15)
    return r.text[:5000]   # bara test nu


def save(data):
    with open("/data/data.json", "w") as f:
        json.dump({"raw": data}, f)


def main():
    print("Worker started")

    while True:
        try:
            data = fetch_data()
            save(data)
            print("Saved data")
        except Exception as e:
            print("ERROR:", e)

        time.sleep(3600)


if __name__ == "__main__":
    main()
