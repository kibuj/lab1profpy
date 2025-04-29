class Machine(object):
    def __init__(self, cost, speed, production_date):
        self.cost = cost
        self.speed = speed
        self.production_date = production_date

class Plane(Machine):
    def __init__(self, cost, speed, production_date, height, passengers):
        super().__init__(cost, speed, production_date)
        self.height = height
        self.passengers = passengers

class Ship(Machine):
    def __init__(self, cost, speed, production_date, passengers, end_place):
        super().__init__(cost, speed, production_date)
        self.end_place = end_place
        self.passengers = passengers


