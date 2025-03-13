#make an empty list of numbers
list_of_numbers = []
#make a function that displays the number lowest to highest
def lowest_to_highest():
    #make a loop that asks for input until the input is invalid and print numbers lowest to highest
    while True:
        try:
            number = int(input("Enter a number: "))
            #check if input is not in the list of number
            #add input to list of numbers if true
        except ValueError:
            break
    #if input is invalid, sort the list of numbers
    #print the list of numbers
#call the function
lowest_to_highest()