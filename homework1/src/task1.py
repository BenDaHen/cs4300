#Task 1

#Function to print out Hello World into the console
def helloWorld():
    print("Hello, World!")

#Pytest
def test_answer(capsys):
    helloWorld()
    #Capture the output in the console
    output = capsys.readouterr()
    assert output.out == "Hello, World!\n"