#initialize the first number
first_number = int(input("Enter a number: "))
#input 9 remaining numbers
for remaining_numbers in range(9):
    remaining_numbers = int(input("Enter a number: "))
    #subtract remaining numbers to first number
    first_number -= remaining_numbers
#print result
print(first_number)