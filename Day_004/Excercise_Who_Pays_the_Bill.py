import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1: Code Solution
#print(random.choice(friends))

#Option 2: Code Solution
random_index = random.randint(0, 4)
print(friends[random_index])