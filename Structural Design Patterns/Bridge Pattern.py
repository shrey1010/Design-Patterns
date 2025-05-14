class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        print("TV is now ON.")

    def turn_off(self):
        print("TV is now OFF.")

class Radio(Device):
    def turn_on(self):
        print("Radio is now ON.")

    def turn_off(self):
        print("Radio is now OFF.")

class Remote:
    def __init__(self, device):
        self.device = device

    def power_on(self):
        self.device.turn_on()

    def power_off(self):
        self.device.turn_off()

# Use Remote with TV
tv = TV()
tv_remote = Remote(tv)

tv_remote.power_on()
tv_remote.power_off()

print()

# Use Remote with Radio
radio = Radio()
radio_remote = Remote(radio)

radio_remote.power_on()
radio_remote.power_off()
