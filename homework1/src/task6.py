#Task 6

#Function to get the word count of a file
def getWordCount():
    wordCount = 0

    #Open the file
    with open(r'/home/student/cs4300/homework1/task6_read_me.txt', 'r') as file:
        #Read the file
        data = file.read()

        #Split the file into words and update the count
        word = data.split()
        wordCount += len(word)

    return wordCount