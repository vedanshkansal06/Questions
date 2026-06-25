from abc import ABC, abstractmethod
class Inverter(ABC):
    def __init__(self,name, current, operating_voltage, energy_generated, energy_used):
        self.name = name
        self.current = current
        self.operating_voltage = operating_voltage
        self.energy_generated = energy_generated
        self.energy_used = energy_used

    def get_name(self):
        print("Inverter Name:", self.name)

    def power_rating(self):
        power_rating = self.current * self.operating_voltage
        print(f"Power Rating: {power_rating}W")

    @abstractmethod
    def get_status(self): pass

class HomeInverter(Inverter):
    def __init__(self,name ,current, operating_voltage, energy_generated, energy_used):
        Inverter.__init__(self, name, current, operating_voltage, energy_generated, energy_used)

    def get_status(self):
        if self.energy_generated <= 0:
            print("No energy generated. Running on grid/battery.")
            return
        battery_percentage = (self.energy_generated - self.energy_used) / self.energy_generated * 100
        if 0 <= battery_percentage < 100: print("Charging")
        elif battery_percentage == 100: print("Charge Completed!")
        else: print("Battery Overload!")

class SolarInverter(Inverter):
    def __init__(self, name, current, operating_voltage, energy_generated, energy_used, panel_rating):
        Inverter.__init__(self, name, current, operating_voltage, energy_generated, energy_used)
        self.panel_rating = panel_rating

    def get_status(self): pass

    def get_panel_rating(self):
        print(f"Panel Rating: {self.panel_rating} W/sec")

class PCU(HomeInverter, SolarInverter):
    def __init__(self, name, current, operating_voltage, energy_generated, energy_used, panel_rating):
        HomeInverter.__init__(self, name, current, operating_voltage, energy_generated, energy_used)
        SolarInverter.__init__(self, name, current, operating_voltage, energy_generated, energy_used, panel_rating)


class GTI(SolarInverter):
    def __init__(self, name, current, operating_voltage, energy_generated, energy_used, panel_rating):
        super().__init__(name, current, operating_voltage, energy_generated, energy_used, panel_rating)

    def get_status(self):
        energy_sold = self.energy_generated - self.energy_used
        if energy_sold < 0: print("System Overload!")
        else: print(f"Energy Sold = {energy_sold} W/sec")

class Regalia(SolarInverter):
    def __init__(self, name, current, operating_voltage, energy_generated, energy_used, panel_rating):
        super().__init__(name, current, operating_voltage, energy_generated, energy_used, panel_rating)

    def get_status(self):
        if self.energy_generated <= 0:
            print("No energy generated. Running on grid/battery.")
            return
        battery_percentage = (self.energy_generated - self.energy_used) / self.energy_generated * 100
        if 0 <= battery_percentage < 100:
            print("Charging, Energy not sold.")
        elif battery_percentage == 100:
            print("Charge Completed!, Energy not sold.")
        else:
            print("System Failure!")

def main():
    zelio = HomeInverter("Zelio", 10, 480, 500, 300)
    zelio.get_name()
    zelio.power_rating()
    zelio.get_status()
    print()

    icruze = HomeInverter("iCruze", 10, 480, 500, 300)
    icruze.get_name()
    icruze.power_rating()
    icruze.get_status()
    print()

    pcu = PCU("PCU", 10, 480, 500, 300, 100)
    pcu.get_name()
    pcu.power_rating()
    pcu.get_status()
    pcu.get_panel_rating()
    print()

    gti = GTI("GTI", 10, 480, 500, 300, 100)
    gti.get_name()
    gti.power_rating()
    gti.get_status()
    gti.get_panel_rating()
    print()

    regalia = Regalia("Regalia", 10, 480, 500, 300, 100)
    regalia.get_name()
    regalia.power_rating()
    regalia.get_status()
    regalia.get_panel_rating()
    print()

if __name__ == "__main__":
    main()



