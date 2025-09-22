#Task 3

#Function to check if a number is positive or negative
def posOrNeg(x):
    #Check if x is positive
    if(x > 0):
        return "Positive"
    #Check if x is negative
    elif(x < 0):
        return "Negative"
    #Otherwise, x should be 0
    else:
        return "Zero"

def primeNumbers():
    #To be a prime number, it must be greater than 1
    # and only divisible by itself

    #Define booleans for determining if multiples are available
    twoMultiple = True
    threeMultiple = True
    fiveMultiple = True
    sevenMultiple = True

    isPrime = True
    #Print only the first 10 primes
    #First 10 primes only go up to 29
    for j in range(30):
        #Check if greater than 1
        if(j > 1):  
            #Check multiples of 2
            if(j%2 == 0 and twoMultiple == True):
                print(j)
                twoMultiple = False
            #Check multiples of 3
            elif(j%3 == 0 and threeMultiple == True):
                print(j)
                threeMultiple = False
            #Check multiples of 5
            elif(j%5 == 0 and fiveMultiple == True):
                print(j)
                fiveMultiple = False
            #Check multiples of 7
            elif(j%7 == 0 and sevenMultiple == True):
                print(j)
                sevenMultiple = False
            #Check numbers with no multiples
            elif(j%2 != 0 and j%3 != 0 and j%5 != 0 and j%7 != 0):
                print(j)

#Function to get the sum of numbers 1 to 100
def sumTo100():
    total = 0
    i = 0
    while(i < 101):
        total += i
        i = i+1

    return total