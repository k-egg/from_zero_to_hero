import pytest
from main import function

def test_function():
    y = function(21.7)
    assert(y==21.7)
