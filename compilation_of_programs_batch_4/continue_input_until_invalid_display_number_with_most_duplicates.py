#define a function that gets the number with the most duplicates from the input
def number_with_most_duplicates():
    #make an empy list of numbers
    list_of_numbers = []
#ask user for input until input is invalid
    while True:
        try:
            number = int(input("Enter a number: "))
            #add input to the list
            list_of_numbers.append(number)
        except ValueError:
            #check which number in the list has the most duplicates
            number_with_most_duplicates = max(list_of_numbers, key = list_of_numbers.count)
            #print the number with the most duplicates
            print(number_with_most_duplicates)
            break

number_with_most_duplicates()