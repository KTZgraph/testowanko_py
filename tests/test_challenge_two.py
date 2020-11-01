import unittest
from challenge_two import Car, CarError


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        # Todo: use the object car to add speed 4 times.
        # Todo: make sure that the current speed is 20.
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 20)

    def test_easy_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to stop the car.
        # Todo: make sure that the current speed is 0 not -10.
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        # dobre praktyki
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        self.car.stop()
        self.car.turn_off_car()
        self.car = None # tak naprawdę nie trzeba bo po użyciu projektu python i tak używa garbage collectora


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        # Todo: raise an exception if the user tried to start the car while it's already on.
        with self.assertRaises(CarError):
            self.car.start_car()

    def test_medium_input_two(self):
        # Todo: use the object car to remove speed 4 times.
        # Todo: raise an exception if the user tried to turn off the car in a speed greater than 0.
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()

        with self.assertRaises(CarError):
            self.car.turn_off_car()

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class HardTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to remove speed 4 times.
        # Todo: make sure that the current speed is 0.
        self.car.add_speed()
        self.car.add_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()

        self.assertEqual(self.car.current_speed(), 0)

    def test_hard_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: make sure that the current speed is 0.
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.car.stop()
        self.car.stop()

        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()