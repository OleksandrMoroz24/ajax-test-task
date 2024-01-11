import subprocess


def get_first_device():
    try:
        result = subprocess.run(
            ["adb", "devices"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            print("Error:", result.stderr)
            return None

        lines = result.stdout.splitlines()
        if len(lines) > 1:
            # The first device is on the second output line (the first line is the header)
            first_device_line = lines[1].strip()
            if first_device_line:
                first_device = first_device_line.split()[0]
                return first_device
        else:
            print("No connected devices.")
            return None

    except FileNotFoundError:
        print("ADB is not installed.")
        return None


def android_get_desired_capabilities():
    first_device_udid = get_first_device()
    if not first_device_udid:
        first_device_udid = "emulator-5554"  # default value
    return {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": first_device_udid,
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
    }
