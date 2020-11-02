import sys
import unittest
from io import StringIO
from console_printed_output import Profile


class TestPrintedOutput(unittest.TestCase):
    """
    Testowanie outputu z konsoli który zwraca funkcja print()
    """

    def setUp(self) -> None:
        self.held, sys.stdout = sys.stdout, StringIO() # liseneren, ta linia nasłuchuje czy coś zostało wypisane na konsole
        self.profile = Profile("Imie Nazwisko", 80, "student")

    def test_name(self):
        """
        metoda zwracajaca sys.stdout.getvalue() ma na koncu nową linię - zwraca "Imie Nazwisko\n"
        :return:
        """
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), "Imie Nazwisko")

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), "80")

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), "student")

    def tearDown(self) -> None:
        self.profile = None