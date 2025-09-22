#Task 2

#Function to test for integers
def integers():
    integer1 = 5
    integer2 = 2
    return integer1 + integer2

#Function to test for floats
def floats():
    float1 = 5.5
    float2 = 6.7
    return float1 + float2

#Function to test for strings
def strings():
    string1 = "Hello"
    string2 = "World"
    return string1 + string2

#Function to test for booleans
def booleans():
    boolean = True
    return boolean

#Pytest for integers
def test_integers():
    assert integers() == 7

#Pytest for floats
def test_floats():
    assert floats() == 12.2

#Pytest for strings
def test_strings():
    assert strings() == "HelloWorld"

#Pytest for booleans
def test_booleans():
    assert booleans() == True