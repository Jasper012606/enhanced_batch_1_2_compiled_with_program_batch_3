#make an empty list
list_of_numbers = []
#define a function that asks user to input a number until the number is invalid
def valid_number():
    while True:
        try:
        #check if input is valid
            number = int(input("Enter a number: "))
            #check if number is in the list
            if number in list_of_numbers:
                #print duplicate if true
                print("Duplicate")
                #print unique if not true
            else:
                print("Unique")
                    #add number to the list
                list_of_numbers.append(number)
        except ValueError:
            break
#call the function
valid_number()
