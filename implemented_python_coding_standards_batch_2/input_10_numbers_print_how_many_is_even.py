#initialize even count to 0
even_count = 0
#input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    #check if even
    if number % 2 == 0: 
        #add 1 to even count if true
        even_count += 1
#print even count