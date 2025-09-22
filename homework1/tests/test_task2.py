#Test Task 2

#Import test2.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task2

#Pytest for integers
def test_integers():
    assert task2.integers() == 7

#Pytest for floats
def test_floats():
    assert task2.floats() == 12.2

#Pytest for strings
def test_strings():
    assert task2.strings() == "HelloWorld"

#Pytest for booleans
def test_booleans():
    assert task2.booleans() == True