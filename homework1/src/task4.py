#Task 4

#Function to calculate a discount
def calculate_discount(price, discount):
    #Discount is the percentage off of 100% (original price)
    newPrice = price * (100-discount)/100
    return newPrice