#make an empty list
list_of_numbers = []
#define a function that asks user to input a number until the number is invalid
def valid_number():
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            break
        #check if input is valid
            #check if number is in the list
                #print duplicate if true
                #print unique if not true
                    #add number to the list
#call the function
valid_number()