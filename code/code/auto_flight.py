"""
AgriEye – Autonomous Flight (Starter)
Waypoint navigation logic (simulation)
"""

WAYPOINTS = [
    (23.7806, 90.2794),
    (23.7810, 90.2800),
    (23.7815, 90.2798),
]

def get_current_position():
    # Fake GPS data for now
    return (23.7806, 90.2794)

def navigate():
    print("Autonomous Mode Active")
    for wp in WAYPOINTS:
        print(f"Navigating to waypoint: {wp}")

def auto_mode():
    current_pos = get_current_position()
    print(f"Current Position: {current_pos}")
    navigate()
    print("Mission Complete")

if __name__ == "__main__":
    auto_mode()
