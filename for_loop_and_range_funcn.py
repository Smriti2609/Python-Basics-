#using for loops with range function

for number in range(0, 11): #for printing numbers between 0 to 10
    print(number)


for number in range(0, 100, 10):  #the last or third number in the bracket indicates by how much the number in the range should be stepped. 
    print(number)


#another example
#The Gauss challenge (adding numbers from 1 to 100)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)

