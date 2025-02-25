
import pytest
from string_calculator import StringCalculator

#empty string test
def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0

def test_single_number():
    calc = StringCalculator()
    assert calc.add("1") == 1
    assert calc.add("5") == 5

