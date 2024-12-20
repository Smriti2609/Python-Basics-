#basically, python uses Mersenne twister for randomisation. But here, we use a random module which python team has already created.
# you can review the documents through this link (https://docs.python.org/3/library/random.html)
#random number integer is generated by random.randint(a,b)

 
#import random
#random_integer = random.randint(a: 1 , b: 10)
#print(random_integer)

#for random integer number generation
import random
random_integer = random.randint(1 , 10)
print(random_integer)

#we can also work in a group creating our own module inside the main file i.e. randomisation here and we can print that using 
#print(file name inside folder.variable used to denote the information inside that file (example below))

#print(my_module.my_favourite_number)

#for random floating points generation= random.random() is used
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#for generation of floating points by multiplication.
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

 # we can also use another function as random floating point generator
random_float = random.uniform(1,10)
print(random_float)



#to print heads ot tails based on randomm number
import random
print("Display Heads or Tails based on random number")
random_heads_or_tails = random.randint(0 , 1)
if (random_heads_or_tails) == 0:
    print("Heads")
else:
    print("Tails")

