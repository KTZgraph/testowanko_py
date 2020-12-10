"""
author: pawlaczyk.
date: Dec, 11, 2020.
To use this class you neded to do: 1- bla bla. 2- bla bla. 3- bla bla.
Extension module = ListChanger().

The reason why we have this is class is because: 1- bla bla. 2- bla bla.
"""

import heapq


class ListChanger:
    def __init__(self, input_list: list):
        self._list = input_list

    # This method is going to return reversed list.
    def reverse_list(self):
        self.__my_private_method() # do testow pkt 3 . debugowanie
        return self._list[::-1]

    # This method is going to return reversed list.
    def has_duplicates(self):
        return len(self._list) != len(set(self._list))

    # This method is going to return reversed list.
    def smallest_number(self):
        return min(self._list)

    # Komentarz to jedno pełno zdanie z kropka na koncu.
    def greatest_number(self):
        return max(self._list)

    # TKomentarz powinien znajdowac sie nad skomplikowana linia kodu.
    def second_greatest_number(self):
        # heap.nlargest is going to get the second larger number in a list.
        return heapq.nlargest(2, set(self._list))[1]

    # This method is going to return reversed list.
    def remove_first_and_last(self):
        return self._list[1:len(self._list) - 1]

    def __my_private_method(self):
        return True

# Programista z opisu pliku moze wywnioskowac jak uzyc klasy.
list_changer = ListChanger()