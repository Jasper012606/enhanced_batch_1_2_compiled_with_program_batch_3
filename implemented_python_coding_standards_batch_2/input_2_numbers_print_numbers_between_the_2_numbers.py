#input two  numbers
first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
#check which number is greater
    #if first number is greater
if first_number > second_number:
        #print all numbers between the second number and first number
    for i in range(second_number, first_number):
        print(i)
elif first_number < second_number:
    for i in range(first_number, second_number):
        print(i)
    #if second number is greater
        #print all numbers between the first number and second number