print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")

pepperoni = input("Do you want pepporoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: Work out how much they need to pay based on their size choice. 
bill = 0 
if size == "S":
    bill += 15
    print("For a small pizza size you pay $15.")
elif size == "M": 
    bill += 20 
    print("For a medium pizza size you pay $20.")
elif size == "L":
     bill += 25 
     print("For a large pizza size you pay $25.")
else: 
     print("You typed the wrong inputs, please type S, M, or L")

# todo: Work out how much to add to their bill based on their pepporoni choice. 
if pepperoni == "Y": 
     if size == "S": 
         bill += 2
     else:
          bill += 3

# todo: Work out their final amount based on wheteher if they want extra cheese. 
if extra_cheese == "Y": 
     bill += 1 

print(f"Your final bill is: ${bill}.")
