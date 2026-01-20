"""
AgriEye – Autonomous Flight Mode (Simulation)
"""

from obstacle_avoidance import check_for_obstacle

WAYPOINTS = [
    (23.7806, 90.2794),
    (23.7810, 90.2800),
    (23.7815, 90.2798),
]

def auto_mode():
    print("Autonomous Mode Active")

    for wp in WAYPOINTS:
        print(f"Heading to waypoint: {wp}")

        obstacle = check_for_obstacle()
        if obstacle:
            print("Changing path to avoid obstacle")
            break

    print("Autonomous mission ended safely")
