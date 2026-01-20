"""
AgriEye – Manual RC Control (Starter)
Reads RC input values (simulated for now)
"""

def read_rc_input():
    # Placeholder values (1000–2000 typical RC range)
    throttle = 1500
    roll = 1500
    pitch = 1500
    yaw = 1500

    return throttle, roll, pitch, yaw

def manual_mode():
    throttle, roll, pitch, yaw = read_rc_input()
    print("Manual Mode Active")
    print(f"Throttle: {throttle}")
    print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")

if __name__ == "__main__":
    manual_mode()
