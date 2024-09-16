#Creating a loop with For and Range to go from 1 to 100. 
for number in range (1, 101): 
    #Checking if number is divisible by both 3 and 5. 
    if number % 3 == 0 and number % 5 == 0: 
        print ("FizzBuzz")
    #Review if number is only divisible by 3 or 5
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    #If it's not divisible by either of those numbers, print the number
    else: 
        print(number)
        