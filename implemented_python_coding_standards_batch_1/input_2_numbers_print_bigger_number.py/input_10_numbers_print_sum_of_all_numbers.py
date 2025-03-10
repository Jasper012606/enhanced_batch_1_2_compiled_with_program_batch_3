#initialize sum to 0
sum = 0
#input 10 numbers
for i in range(10):
    number_to_add = int(input("Enter number: "))
    #add each number to sum
    sum += number_to_add
#print sum
print(sum)