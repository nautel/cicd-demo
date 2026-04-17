import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

print(os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from calculator import add, subtract, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_substract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
