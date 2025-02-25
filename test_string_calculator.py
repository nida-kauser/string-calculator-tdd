
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

def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,2") == 3
    assert calc.add("10,20") == 30

def test_newline_delimiter():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6

def test_different_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3
    assert calc.add("//#\n4#5") == 9
