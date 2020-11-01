import unittest

from first_project import avg


class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_easy_input_two(self):
        self.assertEqual(avg(10, 10, 10, 10, 10), 10)

    def test_easy_input_three(self):
        # True jest traktowane jako liczba 1
        self.assertEqual(avg(1, 1, 1, 1, 1, True), 1)


class MediumTestCase(unittest.TestCase):
    """
    MEdium test - zawsze testowanie dla złych dancyh
    """
    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, "Mohammad"), 2)

    def test_medium_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, 10, "10"), 10)


class HardTestCase(unittest.TestCase):
    """
    Podobne do medium ale raczej user nietechniczny rczej takich danych nie poda
    Raczej etsty bezpieczenstwa
    """

    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1,2,3,4, None), 2)

    def test_hard_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, 10, float), 10)

    def test_hard_input_three(self):
        # not significat
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, 10, frozenset), 10)

    def test_hard_input_three(self):
        #not significat
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, 10, set), 10)

    # def test_hard_input_three(self):
    #     #not significat
    #     with self.assertRaises(TypeError):
    #         self.assertEqual(avg(10, 10, 10, 10, 10, True), 10)



if __name__ == "__main__":
    unittest.main()