import pytest
from .onefile import doubler
from .twofile import squarer

def test_onefile():
    assert 1 == squarer(1) 
    assert 4 == squarer(2)
