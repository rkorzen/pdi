"""
"""

class ElectricCar:

    def __init__(self):
        self.max_range = 100
        self.traveled_distance = 0
    def drive(self, distance):
        if distance < self.max_range - self.traveled_distance:
            self.traveled_distance = distance
            return distance
        else:
            to_travel = self.max_range - self.traveled_distance
            self.traveled_distance = self.max_range
            return to_travel

    def charge(self):
        self.traveled_distance = 0



car = ElectricCar()
assert car.drive(70) == 70
assert car.drive(70) == 30
assert car.drive(10) == 0
car.charge()

assert car.drive(110) == 100

