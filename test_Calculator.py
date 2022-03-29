import pytest
import Calculator

@pytest.mark.parametrize("a,b,c", [(3,2,5),(10,12,15),(2,5,8),(7,8,15)])
def test_add(a,b,c):
    result = Calculator.add(a, b)
    assert c==result

@pytest.mark.parametrize("a,b,c", [(7,2,5),(12,10,2),(12,5,7),(8,6,2)])
def test_sub(a,b,c):
    result = Calculator.sub(a, b)
    assert c==result

@pytest.mark.parametrize("a,b,c", [(1,5,5),(10,12,120),(2,5,10),(7,8,56)])
def test_mul(a,b,c):
    result = Calculator.mul(a, b)
    assert c==result

@pytest.mark.parametrize("a,b,c", [(4,2,2),(100,4,25),(2,5,8),(7,8,15)])
def test_div(a,b,c):
    result = Calculator.div(a, b)
    assert c==result