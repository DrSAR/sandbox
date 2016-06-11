import pytest
from .threefile import reducer

def test_threefile():
    assert 5 == reducer(9) 
