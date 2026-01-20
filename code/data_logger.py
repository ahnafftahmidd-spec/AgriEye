"""
AgriEye – Data Logger
Logs flight data to a CSV file
"""

import csv
from datetime import datetime

LOG_FILE = "flight_log.csv"

def log_data(waypoint, ai_data, obstacle):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            waypoint,
            ai_data["crop_health"],
            ai_data["dry_area"],
            obstacle
        ])

    print("Flight data logged")
