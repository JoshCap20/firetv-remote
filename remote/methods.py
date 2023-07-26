from remote.utils import run_command, is_adb_available, is_device_connected


def connect(ip, port=5555):
    return run_command(["adb", "connect", ip + ":" + str(port)])


def disconnect(ip, port=5555):
    return run_command(["adb", "disconnect", ip + ":" + str(port)])


def check_connection(ip, port=5555):
    return is_adb_available() and is_device_connected(ip, port)


def key_up():
    return run_command(["adb", "shell", "input", "keyevent", "19"])


def key_down():
    return run_command(["adb", "shell", "input", "keyevent", "20"])


def key_left():
    return run_command(["adb", "shell", "input", "keyevent", "21"])


def key_right():
    return run_command(["adb", "shell", "input", "keyevent", "22"])


def key_enter():
    return run_command(["adb", "shell", "input", "keyevent", "66"])


def key_back():
    return run_command(["adb", "shell", "input", "keyevent", "4"])


def key_home():
    return run_command(["adb", "shell", "input", "keyevent", "3"])


def key_menu():
    return run_command(["adb", "shell", "input", "keyevent", "82"])


def key_playpause():
    return run_command(["adb", "shell", "input", "keyevent", "85"])


def key_previous():
    return run_command(["adb", "shell", "input", "keyevent", "88"])


def key_next():
    return run_command(["adb", "shell", "input", "keyevent", "87"])


def key_volume_up():
    return run_command(["adb", "shell", "input", "keyevent", "24"])


def key_volume_down():
    return run_command(["adb", "shell", "input", "keyevent", "25"])


def key_volume_mute():
    return run_command(["adb", "shell", "input", "keyevent", "164"])


def key_power():
    return run_command(["adb", "shell", "input", "keyevent", "26"])


if __name__ == "__main__":
    connect("192.168.1.33")
    key_up()
    key_down()
    key_left()
    key_right()
    key_enter()
    key_back()
    key_home()
    key_menu()
    key_playpause()
    key_previous()
    key_next()
    key_volume_up()
    key_volume_down()
    key_volume_mute()
    key_power()
