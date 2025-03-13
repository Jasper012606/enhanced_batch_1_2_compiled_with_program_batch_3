#define a function that gets the highest to lowest number from the input
def highest_to_lowest():
    #make an empty list of numbers
    list_of_numbers = []
    #ask user for input until input is invalid
    while True:
        try:
            number = int(input("Enter a number: "))
    #add input to the list
        except ValueError:
            break
    #if input is invalid
        #sort the list of numbers
        #print the list of numbers
highest_to_lowest()