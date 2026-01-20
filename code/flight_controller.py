"""
AgriEye – Flight Controller
Switches between Manual and Autonomous modes
"""

from manual_control import manual_mode
from auto_flight import auto_mode

def select_mode(mode):
    if mode == "MANUAL":
        manual_mode()
    elif mode == "AUTO":
        auto_mode()
    else:
        print("Invalid mode selected")

def main():
    print("AgriEye Flight Controller Started")
    mode = "AUTO"  # Change to MANUAL anytime
    select_mode(mode)

if __name__ == "__main__":
    main()
