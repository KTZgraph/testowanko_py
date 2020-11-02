import sys
import unittest
from io import StringIO
from challenge_three import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        # Todo: setup the system to record console printed output.
        # Todo: create an object from the Printer class named printer.
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        # Todo: use the object printer to add the name 'Muhammad Ali' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Muhammad Ali'
        self.printer.set_value('Muhammad Ali')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Muhammad Ali') #strip() do usuwania \n na końcu z konsolowego outputu

    def test_value_job(self):
        # Todo: use the object printer to add the job 'Boxer' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Boxer'
        self.printer.set_value("Boxer")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Boxer") #strip() do usuwania \n na końcu z konsolowego outputu

    def tearDown(self):
        # Todo: set the printer object to None.
        self.printer = None


if __name__ == '__main__':
    unittest.main()