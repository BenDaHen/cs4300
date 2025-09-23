#Test Task 7

#Import task7.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task7

def test_numpy(capsys):
    task7.useNumpy()

    #Capture the output in the console
    output = capsys.readouterr()
    assert output.out == "[[ 6  8]\n [10 12]]\n"