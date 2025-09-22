#Test Task 6

#Import task6.py
import sys
sys.path.append('/home/student/cs4300/homework1/src')
import task6

#Word Count Pytest
def test_wordCount():
    assert task6.getWordCount() == 127