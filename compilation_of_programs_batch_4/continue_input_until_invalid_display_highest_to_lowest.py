#define a function that gets the highest to lowest number from the input
def highest_to_lowest():
    #make an empty list of numbers
    list_of_numbers = []
    #ask user for input until input is invalid
    while True:
        try:
            number = int(input("Enter a number: "))
        #add input to the list
            list_of_numbers.append(number)
        #if input is invalid
        except ValueError:
            #sort the list of numbers from highest to lowest
            list_of_numbers.sort(reverse = True)
            #print the list of numbers
            print(list_of_numbers)
            break
   
highest_to_lowest()