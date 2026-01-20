"""
AgriEye – Autonomous Flight Mode (Simulation)
"""

from obstacle_avoidance import check_for_obstacle
from ai_vision import run_ai_vision

WAYPOINTS = [
    (23.7806, 90.2794),
    (23.7810, 90.2800),
    (23.7815, 90.2798),
]

def auto_mode():
    print("Autonomous Mode Active")

    for wp in WAYPOINTS:
        print(f"Flying to waypoint: {wp}")

        # AI Vision Check
        ai_results = run_ai_vision()

        if ai_results["dry_area"]:
            print("Dry area detected – marking location")

        # Obstacle Avoidance
        obstacle = check_for_obstacle()
        if obstacle:
            print("Obstacle detected – rerouting")
            break

    print("Autonomous mission completed safely")
