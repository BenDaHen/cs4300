#Import test3.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task3

#Positive or Negative Pytest
def test_posOrNeg():
    assert task3.posOrNeg(5) == "Positive"
    assert task3.posOrNeg(-5) == "Negative"
    assert task3.posOrNeg(0) == "Zero"

#Prime Number Pytest
def test_primes(capsys):
    task3.primeNumbers()

    #Capture the output in the console
    output = capsys.readouterr()
    assert output.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

#Sum Pytest
def test_sum():
    assert task3.sumTo100() == 5050