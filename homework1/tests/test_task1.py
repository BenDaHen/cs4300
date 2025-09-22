#Test Task 1

#Import Task 1
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task1

#Pytest
def test_answer(capsys):
    task1.helloWorld()
    #Capture the output in the console
    output = capsys.readouterr()
    assert output.out == "Hello, World!\n"