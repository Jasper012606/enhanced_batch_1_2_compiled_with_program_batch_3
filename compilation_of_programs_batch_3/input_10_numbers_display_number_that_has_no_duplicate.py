#make an empty list
list_of_numbers = []
#input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    #add numbers to the list
    list_of_numbers.append(number)
    
#make an empty list of numbers without duplicates
number_without_duplicates = []
#check if number in numbers has no duplicates
for number in list_of_numbers:
    if list_of_numbers.count(number) == 1:
    #add number to the list if true
        number_without_duplicates.append(number)
    
#print numbers without duplicates
print(number_without_duplicates)