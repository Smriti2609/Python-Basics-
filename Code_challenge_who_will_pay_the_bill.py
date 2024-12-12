import random
print("Who will pay the bill?")
friends = ["Buney", "Hali", "Nyauri", "Mausi", "Ironman", "Seti", "Kanau", "Sara"]
#option 1st
print(random.choice(friends))#random.choice(seq) can be used to print the random name from the sequence
#option 2
random_index = random.randint(0 , 7)
print(friends[random_index]) #random name from the sequence will be generated here by the mentioned commands.

print(f"The person who will pay the bill is: {random.choice(friends)}")



###index errors and working with nested lists.
print(len(friends))  #it will give the no of friends in the list.

print(friends[6]) #it will print the 6th name in the list of friend counting from 0 to 7

#print(friends[9]) #this command it will throw an index error.



#working with nested list.
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, Vegetables]
print(dirty_dozen)