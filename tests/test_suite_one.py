import unittest
from tests.test_new import TestCalculate, TestGetNetWorth, TestGetApartmentsNeeded

"""
Organizacja testów, kiedy plików testowych zaczyna być dużo, powinny być zorganizowane według featerów
W aplikacja zastanawiać się, które testy powinny być uruchomione do dane feature i tak je organizować
folder tests to dobry początek, ale przy dużych projektach to nie wystarcza
Sprawia, ze testy sa dużo lepiej zorganizowane
"""


def suite():
    """
    Powinien byc test dla każdegego feature
    - to jest garśc testów zgrupowanych ze sobą
    tutaj uruchamia 6 wybranych testów 9różne metody z różnych klas testujacych)
    """
    suite = unittest.TestSuite()

    # do obiektu suit dodajemy wybrana metodą klasy testów - konkretny pojedynczy test
    suite.addTest(TestCalculate('test_calculate_easy_first'))
    suite.addTest(TestCalculate('test_calculate_medium_first'))
    suite.addTest(TestCalculate('test_calculate_hard_first'))

    suite.addTest(TestGetNetWorth('test_net_worth_easy_first'))
    suite.addTest(TestGetNetWorth('test_net_worth_easy_second'))

    suite.addTest(TestGetApartmentsNeeded('test_apartments_needed_easy_first'))

    return suite


if __name__ == "__main__":
    # obiket potrzebny do uruchomienia wybranych w funckji testów
    runner = unittest.TextTestRunner()
    runner.run(suite())