#Test Task 7

#Import task7.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task7

def test_numpy():
    assert task7.useNumpy() == [[6, 8],[10, 12]]