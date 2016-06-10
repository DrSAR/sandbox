import pytest
from .onefile import doubler

def test_onefile():
    assert 2 == doubler(1) 
