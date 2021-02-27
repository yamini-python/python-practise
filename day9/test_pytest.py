import pytest
from doctestdemo import equals

def test_equals():
    assert equals(8,8) == "Equal"

def test_not_equal_num():
    assert equals(8,9) == "Not Equal", "the value should be equal"

@pytest.mark.skip(reason="Skip this test")
def test_skip():
    assert equals(8,9) == "Not Equal"

@pytest.mark.skipif(5==5, reason="condition true in skipif")
def test_skipif_true():
    assert equals(8,8) == "Not Equal"

@pytest.mark.skipif(5==7, reason="condition false in skipif")
def test_skipif_false():
    assert equals(8,8) == "Equal"

@pytest.mark.xfail
def test_function():
    assert equals(6,6) == "Not Equal" 

@pytest.mark.parametrize("test_input,expected", [("8==8", True), ("9*9", 81)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected



@pytest.fixture
def element1():
    return 3

@pytest.fixture
def element2():
    return 2

def test_fixture(element1,element2):
    assert equals(element1,element2) == "Not Equal" 

@pytest.mark.parametrize("element1, element2, expected", [(2,2,"Equal"),(2,3,"Not Equal")])
def test_equals(element1,element2, expected):
    assert equals(element1,element2) == expected

  