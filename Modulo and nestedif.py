 #modulo
#check whether the no is odd or even.
Number = int(input("Enter the number: "))
if Number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#nested if statements and elif statements
#if condition:
#   if another condition:
#        do this
#   else:
#       do this
#else:
#   do this

#example
print("Welcome to the Rollercoaster!")
height = int(input("Enter the height of a rider in cm? cm"))
age = int(input("Enter the age of a rider."))
if height >= 120:
    if age <= 18:
        print("Please pay $7 for ticket.")
    else:
        print("Please pay $12 for ticket..")
else:
    print("Sorry! You need to grow taller to take a ride.")


#if / elif / else

print("Welcome to the Rollercoaster!")
height = int(input("Enter the height of a rider in cm? cm"))
age = int(input("Enter the age of a rider."))
if height >= 120:
    if age <= 12:
        print("Please pay $5 for ticket.")
    elif age > 12: 
        print("Please pay $7 for ticket.")
    elif age <= 18:
         print("Please pay $7 for ticket.")
    elif age > 18:
         print("Please pay $12 for ticket..")
else:
    print("Sorry! You need to grow taller to take a ride.")

