import subprocess


def run_command(command):
    try:
        subprocess.check_call(command)
        return True
    except subprocess.CalledProcessError:
        return False


def is_adb_available():
    try:
        subprocess.check_call(["adb", "version"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def is_device_connected(ip, port=5555):
    try:
        output = subprocess.check_output(["adb", "devices"])
        return "{}:{}\tdevice".format(ip, port) in output.decode("utf-8")
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    print("is_adb_available: {}".format(is_adb_available()))
    print("is_device_connected: {}".format(
        is_device_connected("192.168.1.33")))
