#(we can use the list data structure to store different datas inside a single variable.)
states_of_america = ["Delware", "Pennsylvania", "New Jersey", "Georgia" ] #we can store the states in this way.
print(states_of_america[0]) #this will print the first data in the data structure or list.

print(states_of_america[-2]) #this starts counting from the end which means now,New Jersey is printed. 
states_of_america[1] = "Helware"  #in this way we can modify the data in the list.

states_of_america.append("Smritiland") #append will add the single item at the end of the list.Smritiland will be added to the end of the list.

print(states_of_america) # Now, Helware is printed in place of Delware.

#list.append()= adds a single item to the list.
#list.extend([])= add the who bunch of item to the list.
#list.insert()= inserts an item in the given position.
#list.remove()= removes the first item from the list.
#list.pop()= removes the item at the given position in the list, and return it.
#and so on

