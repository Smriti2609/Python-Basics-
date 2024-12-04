#A and B (for the entire line of code to be true both A and B have to be true.)
#C or D  (for the entire line of code to be true either C or D have to be true.Its also true if C and D both are true and false when they both are false.)
#not E    (reverse i.e it makes the condition T if it is F and F if it is T)


print("Welcome to the Rollercoaster!")
height = int(input("Enter the height of a rider in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter the age of a rider.\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:  
        bill = 7
        print("Youth tickets are $7.")
    elif (age >= 45 and age <= 55):      #can also be written as (elif 45 =< age <=55 )
        bill = 0
        print("Person with midlife crisis falls under this age group and gets ticket for free.") 
    else:        
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")
    if wants_photo == "y":
        if (age >= 45 and age <= 55):
            bill = 0
            print("$0 charge for photos for age group 45 to 55.")
        else:
        #Add $3 to their bill.
            bill += 3 #does the same work as bill = bill + 3
    print(f"Your final bill is\n {bill}")    #{} is used to identify the bill value inside the print statement.
else:
    print("Sorry! You need to grow taller to take a ride.")




#Quick question to review 
# What will the following code print?
# a = 5
# b = 7
# if a >= b and a != b:
#     print("A") 
# elif not a >= b and a != b:
#     print("B")
# else:
#     print("C")

#B will be printed as a=5 and b=7 if not a>=b and a!=b: both  of them are true (True and True) is True for condition B so B is printed.

