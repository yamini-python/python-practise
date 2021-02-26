from doctestdemo import equals

def test_equals():
    assert equals(8,8) == "Equal"

def test_not_equal_num():
    assert equals(8,9) == "Not Equal"

def test_negative_equal():
    assert equals(-3,-3) == "Equal"

def test_equals_strings():
    assert equals('hi','hi') ==  "Equal"

def test_equals_strings2():
    assert equals('hi','hii') ==  "Not Equal" 

