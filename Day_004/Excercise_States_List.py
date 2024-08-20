states_of_america = ["Delaware", "Pennsylvania", "Alabama", "California", "Indiana"]

#print(states_of_america[-2])

states_of_america[1] = "Penny"
#print(states_of_america[1])
#states_of_america.append("Angelaland")
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)