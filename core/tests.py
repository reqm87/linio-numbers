from linio_numbers import LinioNumber
from tests_data import linio_numbers


class TestLinioNumbers(object):
    def test_linio_numbers(self):
        for i in range(1, 101):
            linio_number = LinioNumber(i)
            assert linio_number.process() == str(linio_numbers[i - 1])
