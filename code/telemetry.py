"""
AgriEye – Telemetry System (Simulation)
"""

import random
from datetime import datetime

def get_telemetry_data(mode, waypoint):
    telemetry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "mode": mode,
        "altitude_m": random.randint(40, 60),
        "speed_kmh": random.randint(35, 55),
        "battery_%": random.randint(60, 100),
        "waypoint": waypoint
    }
    return telemetry

def send_telemetry(telemetry):
    print("\n--- TELEMETRY UPDATE ---")
    for key, value in telemetry.items():
        print(f"{key}: {value}")
    print("------------------------\n")
