from abc import ABC, abstractmethod
"""Write a program to depict Indian Politics."""

class Driver:
    def __init__(self, name):
        self.name = name

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class MPS(ABC):
    def __init__(self, name, constituency, driver, expenses):
        self.name = name
        self._constituency = constituency
        self._expenses = expenses
        self._expense_limit = 100000
        self.driver = driver
        self.car = Vehicle("Car")

    def get_constituency(self):
        print(f"{self.name} belongs to {self._constituency}")

    def get_driver(self):
        print(f"Car Driver for {self.name}: {self.driver.name}")

    def exceed_limit(self):
        if self._expenses > self._expense_limit: return True
        else: return False

    def is_arrestable(self):
        return True

    @abstractmethod
    def get_role(self):
        pass

class MP(MPS):
    def get_role(self):
        return "MP"

class Minister(MPS):
    def __init__(self, name, constituency, driver, expenses):
        super().__init__(name, constituency, driver, expenses)
        self._expense_limit = 1000000

    def _arrest_permission(self):  # PM grants arrest permission if expense > 1100000
        if self._expenses > 1100000: return True
        else: return False

    def is_arrestable(self):
        return True if self._arrest_permission() else False

    def get_role(self):
        return "Minister"

class PM(Minister):
    def __init__(self, name, constituency, driver, expenses, pilot):
        super().__init__(name, constituency, driver, expenses)
        self._expense_limit = 10000000
        self.pilot = pilot
        self.plane = Vehicle("Air Craft")

    def get_driver(self):
        print(f"Car Driver: {self.driver.name}, Aircraft Pilot: {self.pilot.name}")

    def is_arrestable(self):
        return False

    def get_role(self):
        return "PM"


class Commissioner:
    def can_arrest(self, politician):
        print(f"{politician.name} {politician.get_role()} is being assessed...")
        if not politician.exceed_limit():
            print("The politician does not exceed the spending limit.")
        else:
            if politician.is_arrestable():
                print("The politician is arrested!")
            else:
                print("The politician is not arrestable!")

def main():
    driver = Driver("Utkarsh")
    pilot = Driver("Krish")
    commissioner = Commissioner()

    mp = MP("Aman", "Aligarh", driver, 110000)
    mp.get_driver()
    mp.get_constituency()
    commissioner.can_arrest(mp)
    print()

    minister1 = Minister("Ishan", "Agra", driver, 1010000)
    minister2 = Minister("Vedansh", "Jaipur", driver, 1200000)
    minister1.get_driver()
    minister1.get_constituency()
    commissioner.can_arrest(minister1)
    print()

    minister2.get_driver()
    minister2.get_constituency()
    commissioner.can_arrest(minister2)
    print()

    pm = PM("Modi" ,"India", driver, 101000000, pilot)
    pm.get_role()
    pm.get_driver()
    pm.get_constituency()
    commissioner.can_arrest(pm)

if __name__ == "__main__":
    main()