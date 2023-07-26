# Wrapper for FireTV using adb
import remote.methods as methods

class Remote:
    def __init__(self, ip: str):
        self.ip: str = ip
        assert methods.is_adb_available(), "ADB not available"
        self.connect()

    def connect(self):
        return methods.connect(self.ip)

    def disconnect(self):
        return methods.disconnect(self.ip)

    def check_connection(self):
        return methods.check_connection(self.ip)

    def up(self):
        return methods.key_up()

    def down(self):
        return methods.key_down()

    def left(self):
        return methods.key_left()

    def right(self):
        return methods.key_right()

    def enter(self):
        return methods.key_enter()

    def back(self):
        return methods.key_back()

    def home(self):
        return methods.key_home()

    def menu(self):
        return methods.key_menu()

    def play(self):
        return methods.key_playpause()

    def pause(self):
        return methods.key_playpause()

    def previous(self):
        return methods.key_previous()

    def next(self):
        return methods.key_next()

    def power(self):
        return methods.key_power()

    def volume_up(self):
        return methods.key_volume_up()

    def volume_down(self):
        return methods.key_volume_down()

    def mute(self):
        return methods.key_volume_mute()


if __name__ == "__main__":
    remote = Remote("192.168.1.33")
    remote.power()