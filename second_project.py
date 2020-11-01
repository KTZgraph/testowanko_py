
class Counter:
    """
    Upenwiamy się że najniższa wartość jaką ma klasa to 0
    """
    def __init__(self):
        self._value = 0

    def add(self):
        self._value += 1

    def remove(self):
        if self._value <= 0:
            # self._value = 0 obojetnie ktore rozwiazanie
            self.clear()
        else:
            self._value -= 1

    def clear(self):
        self._value = 0

    def get_value(self):
        return self._value


# counter = Counter()
# counter.add()
# counter.add()
# counter.add()
# counter.add()
# counter.add()
#
# counter.remove()
# counter.remove()
# counter.remove()
#
# counter.clear()
# print(counter.get_value())