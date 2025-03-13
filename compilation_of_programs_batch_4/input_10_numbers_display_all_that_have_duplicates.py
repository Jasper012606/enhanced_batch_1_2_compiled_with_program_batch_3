#make an empty list of numbers
list_of_numbers = []
#make an empty list of numbers with duplicates
numbers_with_duplicates = []
#input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    #check if number is not in the list
        #add number to the list if true
    if number not in list_of_numbers:
        list_of_numbers.append(number)
        #add number to the list of numbers with duplicates if not true
    else:
        numbers_with_duplicates.append(number)
#print the numbers with duplicates
print(numbers_with_duplicates)
