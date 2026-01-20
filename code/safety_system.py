"""
AgriEye – Safety System
"""

def check_battery(level=80):
    if level < 20:
        print("WARNING: Low Battery!")
        return False
    return True

def check_rc_signal(signal=True):
    if not signal:
        print("RC Signal Lost!")
        return False
    return True
