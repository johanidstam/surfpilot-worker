import json
import time
import os


DATA_DIR = "/data"
DATA_FILE = os.path.join(DATA_DIR, "data.json")


def fetch_real_data():
    return [
        {"operator": "Hallon", "gb": 100, "price": 115},
        {"operator": "Vimla", "gb": 60, "price": 170},
        {"operator": "Comviq", "gb": 50, "price": 185},
        {"operator": "Fello", "gb": 50, "price": 265},
        {"operator": "Telenor", "gb": 100, "price": 279},
    ]


def save(plans):

    # Skapa /data om den inte finns
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump({"plans": plans}, f, indent=2)


def main():

    print("Worker started")

    while True:

        plans = fetch_real_data()
        save(plans)

        print("Data updated")

        time.sleep(10800)  # 3h


if __name__ == "__main__":
    main()
