class Machine(object):
    def __init__(self, cost, speed, production_date):
        self.__cost = cost
        self.__speed = speed
        self.__production_date = production_date

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        if cost >= 0:
            self.__cost = cost

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed

    def get_production_date(self):
        return self.__production_date

    def set_production_date(self, production_date):
        if production_date is not None:
            self.__production_date = production_date

class NotLand(Machine):
    def __init__(self, cost, speed, production_date, passengers):
        super().__init__(cost, speed, production_date)
        self.__passengers = passengers

    def get_passengers(self):
        return self.__passengers

    def set_passengers(self, passengers):
        if passengers >= 0:
            self.__passengers = passengers

class Car(Machine):
    def __init__(self, cost, speed, production_date):
        super().__init__(cost, speed, production_date)

    def __str__(self):
        return f"Car {self.get_cost(), self.get_speed()}, {self.get_production_date()}"

class Plane(NotLand):
    def __init__(self, cost, speed, production_date, height, passengers):
        super().__init__(cost, speed, production_date, passengers)
        self.__height = height


    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height >= 0:
            self.__height = height

    def __str__(self):
        return f"Plane {self.get_cost(), self.get_speed(), self.get_production_date(), self.get_height(), self.get_passengers()}"

class Ship(NotLand):
    def __init__(self, cost, speed, production_date, passengers, end_place):
        super().__init__(cost, speed, production_date, passengers)
        self.__end_place = end_place


    def get_end_place(self):
        return self.__end_place

    def set_end_place(self, end_place):
        if end_place is not None:
            self.__end_place = end_place

    def __str__(self):
        return f"Ship {self.get_cost(), self.get_speed(), self.get_production_date(), self.get_end_place(), self.get_passengers()}"


def main():

    def min_speed(vehicles, min_speed):
        fast_vehicles_list = []
        for v in vehicles:

            if v.get_speed() > min_speed:
                fast_vehicles_list.append(v)

        return fast_vehicles_list

    vehicles = [
        Ship(10000000, 100, "26.07.2005", 12345, "31.04.2025"),
        Car(10000, 200, "26.07.2019",),
        Plane(100000, 600, "26.07.2015", 6, 10)
    ]

    m = min_speed(vehicles, 150)

    for i in m:
        print(i)

main()


