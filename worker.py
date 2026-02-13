import json
import time


def fetch_real_data():
    return [
        {"operator": "Hallon", "gb": 100, "price": 115},
        {"operator": "Vimla", "gb": 60, "price": 170},
        {"operator": "Comviq", "gb": 50, "price": 185},
        {"operator": "Fello", "gb": 50, "price": 265},
        {"operator": "Telenor", "gb": 100, "price": 279},
    ]


import os
import json
import time


def save(plans):

    os.makedirs("/data", exist_ok=True)

    temp_file = "/data/data.tmp"
    final_file = "/data/data.json"

    # Skriv till temp först
    with open(temp_file, "w") as f:
        json.dump({"plans": plans}, f, indent=2)

    # Byt fil atomiskt
    os.replace(temp_file, final_file)

    print("Data saved safely")



def main():

    print("Worker started")

    while True:

        plans = fetch_real_data()
        save(plans)

        print("Data updated")

        time.sleep(10800)  # 3h


if __name__ == "__main__":
    main()
