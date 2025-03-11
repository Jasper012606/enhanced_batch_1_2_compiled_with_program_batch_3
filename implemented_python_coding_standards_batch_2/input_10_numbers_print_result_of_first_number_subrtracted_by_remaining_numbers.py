#initialize the first number
first_number = int(input("Enter a number: "))
#input 9 remaining numbers
for remainding_numbers in range(9):
    remainding_numbers = int(input("Enter a number: "))
    #set the result as the difference of the first number subtracted by the remaining numbers
    result = first_number - remainding_numbers
#print result
print(result)