from calorie_calculator import get_name, get_age

#testing for an age above reasonable limit
def test_get_age():
    assert get_age() == 112

#testing against a blank name
def test_get_name():
    assert get_name() == " "