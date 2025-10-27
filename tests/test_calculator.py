import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1

    def test_factorial(self):
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            self.calc.factorial(-1)

    def test_percentage(self):
        assert self.calc.percentage(50, 100) == 50
        assert self.calc.percentage(25, 200) == 12.5
        assert self.calc.percentage(1, 4) == 25

    def test_percentage_zero_whole(self):
        with pytest.raises(ValueError):
            self.calc.percentage(10, 0)