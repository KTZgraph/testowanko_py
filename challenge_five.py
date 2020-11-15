import heapq


class ListChanger:
    def __init__(self, input_list: list):
        self._list = input_list

    def reverse_list(self):
        return self._list[::-1]

    def has_duplicates(self):
        if len(set(self._list)) < len(self._list):
            return True

        return False

    def smallest_number(self):
        """
        Zwraca najmneijsza z liczb, jeśli lista nie zawiera liczb to zwraca None
        :return:
        """
        number_list = [i for i in self._list if isinstance(i, (int, float))]
        if number_list:
            return min(number_list)

        return None

    def greatest_number(self):
        """
        Zwraca NAJWIEKSZA z liczb, jeśli lista nie zawiera liczb to zwraca None
        :return:
        """
        number_list = [i for i in self._list if isinstance(i, (int, float))]
        if number_list:
            return max(number_list)

        return None

    def second_greatest_number(self):
        # number_list = [i for i in self._list if isinstance(i, (int, float))]
        # if number_list:
        #     number_list = list(set(number_list))
        #     number_list.sort(reverse=True)
        #     return number_list[1]
        return heapq.nlargest(2, set(self._list))[1]

    def remove_first_and_last(self):
        return self._list[1:-1]

