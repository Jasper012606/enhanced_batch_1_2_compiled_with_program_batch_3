#make a function that gets the lowest number from the input
def get_lowest_number():
    #initialize lowest number to None
    lowest_number = None
    #make a loop that asks for input until the input is invalid and print the lowest number
    while True:
        try:
            number = int(input("Enter a number: "))
        #if lowest number is None, set input to lowest number
            #check if next input is less than lowest number
            #set input to lowest number if true
        except ValueError:
            break
#call the function
get_lowest_number()