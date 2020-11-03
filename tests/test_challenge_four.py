import time
import unittest
from challenge_four import EfficiencyAdding


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = dict()

    def test_first_adding_method(self):
        # Todo: start timing your program.
        # Todo: use the object self._efficiency to call the adding_two_first_method.
        # Todo: end timing your program.
        # Todo: add the result to self._efficiency_data dictionary.
        start_time = time.perf_counter()
        self._efficiency.adding_two_first_method(10000)
        end_time = time.perf_counter()
        self._efficiency_data.update({"adding_two_first_method": end_time - start_time})

    def test_second_adding_method(self):
        # Todo: start timing your program.
        # Todo: use the object self._efficiency to call the adding_two_second_method.
        # Todo: end timing your program.
        # Todo: add the result to self._efficiency_data dictionary.
        start_time = time.perf_counter()
        self._efficiency.adding_two_second_method(10000)
        end_time = time.perf_counter()
        self._efficiency_data.update({"adding_two_second_method": end_time - start_time})

    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None
        self._efficiency_data.clear()


if __name__ == '__main__':
    unittest.main()