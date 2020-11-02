import time
import unittest
from efficiency import FibonacciSequence


class TestFibonacciSequence(unittest.TestCase):
    """
    https://docs.python.org/3/library/time.html#time.perf_counter
    time.perf_counter() zwraca dokładniejszy czaas niż time.time() ktorego delta dla matematycznej funckji zwraca 0
    """

    def setUp(self) -> None:
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = dict()

    def test_first_method(self):
        starting_time = time.perf_counter()
        self._fibonacci_sequence.recursive_method(30)
        ending_time = time.perf_counter()
        self._efficiency_data['recursive_method'] = ending_time - starting_time
        print(self._efficiency_data)

    def test_second_method(self):
        starting_time = time.perf_counter()
        self._fibonacci_sequence.math_method(30)
        ending_time = time.perf_counter()
        self._efficiency_data['math_method'] = ending_time - starting_time
        print(self._efficiency_data)

    def tearDown(self) -> None:
        self._fibonacci_sequence = None
        self._efficiency_data.clear() #czyszczenie słownika - pozostaje pusty