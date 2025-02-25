
import pytest
from string_calculator import StringCalculator

#empty string test
def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0


