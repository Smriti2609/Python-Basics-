#if /elif /else          multiple if
#if condition1:          if condition1:
#   do A                    do A 
#elif condition2:        if condition2:
#   do B                    do B
#else:                   if condition3:
#   do C                    do C


print("Welcome to the Rollercoaster!")
height = int(input("Enter the height of a rider in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter the age of a rider.\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:  #Check for youth age first (13-18)
        bill = 7
        print("Youth tickets are $7.")
    else:        #Adult tickets for age above 18 
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")
    if wants_photo == "y":
        #Add $3 to their bill.
        bill += 3 #does the same work as bill = bill + 3
    print(f"Your final bill is\n {bill}")    #{} is used to identify the bill value inside the print statement.
else:
    print("Sorry! You need to grow taller to take a ride.")
