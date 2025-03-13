#define a function that gets the number with the most duplicates from the input
def number_with_most_duplicates():
    #make an empy list of numbers
    list_of_numbers = []
#ask user for input until input is invalid
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            break
#add input to the list
#check which number in the list has the most duplicates
#print the number with the most duplicates
number_with_most_duplicates()