#Test Task 4

#Import test4.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task4

def test_discount():
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(70, 10) == 63
    assert task4.calculate_discount(60, 25) == 45
    assert task4.calculate_discount(69.99, 25) == 52.4925