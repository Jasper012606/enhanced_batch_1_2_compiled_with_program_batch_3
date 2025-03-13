#define a function that gets the average of numbers from the input
def average_of_numbers():
    #initialize number count to 0
    number_count = 0
    #initialize sum of numbers to 0
    sum_of_numbers = 0
    #ask user for input until input is invalid
    while True: 
        try:
            number = int(input("Enter a number: "))
            #for every input, add number to the first number, add 1 to average
            sum_of_numbers += number
            number_count += 1
        except ValueError:
            average = sum_of_numbers / number_count
            print(average)
            break
    #divide the sum of numbers by the average
    #print the average
average_of_numbers()