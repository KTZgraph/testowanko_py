"""Coding Challenge Skeleton #2
"""


class CarError(Exception):
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class Car:
    def __init__(self):
        self._speed = 0
        self._start_car = False

    def start_car(self):
        if self._start_car is False:
            self._start_car = True
        else:
            raise CarError("Car already started")

    def turn_off_car(self):
        if self._speed > 0:
            raise CarError("Unable to turn off car when speed  greater than 0")
        self._start_car = False

    def add_speed(self):
        if self._start_car is False:
            raise CarError("Unable add speed to stopped car")
        self._speed += 5

    def remove_speed(self):
        if self.current_speed() <= 0:
            self._speed = 0
        else:
            self._speed -= 5

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._start_car
