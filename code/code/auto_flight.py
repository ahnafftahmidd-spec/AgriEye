"""
AgriEye – Autonomous Flight Mode (Simulation)
"""

from obstacle_avoidance import check_for_obstacle
from ai_vision import run_ai_vision
from data_logger import log_data
from telemetry import get_telemetry_data, send_telemetry

WAYPOINTS = [
    (23.7806, 90.2794),
    (23.7810, 90.2800),
    (23.7815, 90.2798),
]

def auto_mode():
    print("Autonomous Mode Active")

    for wp in WAYPOINTS:
        print(f"Flying to waypoint: {wp}")

        ai_results = run_ai_vision()
        obstacle = check_for_obstacle()

        telemetry = get_telemetry_data(
            mode="AUTO",
            waypoint=wp
        )
        send_telemetry(telemetry)

        log_data(
            waypoint=wp,
            ai_data=ai_results,
            obstacle=obstacle
        )

        if obstacle:
            print("Obstacle detected – returning to safe mode")
            break

    print("Autonomous mission completed")
