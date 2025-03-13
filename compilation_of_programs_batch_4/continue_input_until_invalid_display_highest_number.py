#define a function that gets the highest number
def get_highest_number():
    #initialize highest number to None
    highest_number = None
    #ask for input until input is invalid then print the highest number
    while True:
        try:
            number = int(input("Enter a number: "))
            #set first input to highest number if highest number is None
            #check if next input is greater than highest number
            if highest_number == None or number > highest_number:
                #set input to highest number if true
                highest_number = number
        except ValueError:
            break
get_highest_number()