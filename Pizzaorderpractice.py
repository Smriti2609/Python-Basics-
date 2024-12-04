print("Welcome to python Pizza Deliveries!")
Bill = 0


Pizza_size = input("What size pizza do you want? Type S for small, type M for medium and type L for large:\n")
if Pizza_size == "S":
    Bill += 15
    print("Your Bill is $15.")
elif Pizza_size == "M":
    Bill += 20
    print("Your bill is $20.")
elif Pizza_size == "L":
    Bill += 25
    print("Your bill is 25$.")
else:
    print("You typed wrong inputs.")

Pepperoni = input("Do you want pepperoni on your pizza? type Y for yes and N for no:\n")
if Pepperoni == "Y":
    if Pizza_size == "S":
        Bill += 2
    else:
        Bill += 3
       
Extra_cheese = input("Do you want extra cheese? Y or N:\n")
if Extra_cheese == "Y":
    Bill += 1
    print(f"Your final bill is: ${Bill}.")
