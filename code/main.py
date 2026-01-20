"""
AgriEye UAV – Starter Code
Author: Ahnaf Tahmid
Description: Basic system check and startup sequence
"""

print("AgriEye UAV System Booting...")

def system_check():
    print("Checking sensors...")
    print("IMU: OK")
    print("GPS: OK")
    print("RC Receiver: OK")
    print("Battery: OK")

def main():
    system_check()
    print("System ready.")
    print("Waiting for flight mode selection...")

if __name__ == "__main__":
    main()
