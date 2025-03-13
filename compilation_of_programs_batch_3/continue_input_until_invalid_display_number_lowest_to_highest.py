#make an empty list of numbers
list_of_numbers = []
#make a function that displays the number lowest to highest
def lowest_to_highest():
    #make a loop that asks for input until the input is invalid and print numbers lowest to highest
    while True:
        try:
            number = int(input("Enter a number: "))
            #add input to list of numbers if true
            list_of_numbers.append(number)
        #if input is invalid, sort the list of numbers
        except ValueError:
            list_of_numbers.sort()
            #print the list of numbers
            print(list_of_numbers)
            break
#call the function
lowest_to_highest()