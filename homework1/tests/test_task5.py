#Test Task 5

#Import task5.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task5

def test_dictionary():
    assert task5.firstBooks() == ["The Witcher", "Fourth Wing", "Percy Jackson"]