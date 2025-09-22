#Test Task 5

#Import task5.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task5

#Books Pytest
def test_books(capsys):
    task5.firstBooks()

    #Capture the output in the console
    output = capsys.readouterr()
    assert output.out == "['The Witcher', 'Fourth Wing', 'Percy Jackson']\n"

#Student Dictionary Pytest
def test_dictionary():
    assert task5.studentDictionary() == {'name': 'Ben', 'studentID': 123456}
    #Check if a dictionary is returned
    assert isinstance(task5.studentDictionary(), dict)