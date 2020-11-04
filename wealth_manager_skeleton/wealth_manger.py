"""
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""


class Calculator:
    def __init__(self, passive_income_desired_yearly, yearly_savings, starting_year, price_of_one_apartment,
                 price_od_renting_one_apartment):
        self._passive_income_desired_yearly = passive_income_desired_yearly
        self._yearly_savings = yearly_savings
        self._starting_year = starting_year
        self._price_of_one_apartment = price_of_one_apartment
        self._price_od_renting_one_apartment = price_od_renting_one_apartment
        self._anser = dict() #odpowiedx w postaci słownika
        self._calculate()