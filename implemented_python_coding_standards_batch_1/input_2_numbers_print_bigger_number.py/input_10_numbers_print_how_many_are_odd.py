#initialize odd_count to 0
odd_count = 0
#input 10 numbers
for i in range(10):
    number = int(input("Enter number: "))
#check if odd
    if number % 2 != 0:
    #add to odd_count if true
        odd_count += 1
#print odd_count
print(odd_count)