"""Coding Challenge Skeleton #1
This counter function purpose is to count how many english letters does your name contain.
After writing your tests, develop the counter function as needed to pass all your tests.
"""


def counter(name:str)->int:
    if name is None:
        raise TypeError("You can't input None values")

    name = name.replace(" ", "")
    if len(name) == 0:
        raise TypeError("Please input your name")
    if not isinstance(name, str):
        raise TypeError("Input is not a string value")
    if not name.isalpha():
        raise TypeError("String contains non english letters")

    return len(name)

