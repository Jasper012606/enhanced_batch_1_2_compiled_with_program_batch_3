#make an empty list 
list_of_numbers = []
#input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    #check if number is not in the list
    if number not in list_of_numbers:
        list_of_numbers.append(number)
        #add number to the list if true
#print the numbers in the list