#Task 5

#Function to get the first three books in a list
def firstBooks():
    books = ["The Witcher", "Fourth Wing", "Percy Jackson", "Book 4", "Book 5", 
    "Andrzej Sapkowski", "Rebecca Yaros", "Rick Riordan", "Author 4", "Author 5"]

    #Get the first three books in the list
    firstThreeBooks = books[:3]
    print(firstThreeBooks)

def studentDictionary():
    #Create a dictionary 
    studentDict = {
        "name": "Ben",
        "studentID": 123456
    }

    return studentDict