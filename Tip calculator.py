print("Welcome to thr Tip Calculator!")
bill = float(input("What was the total bill? $")) #
print(bill)
tip = float(input("What percentage tip would you like to give? 10 12 15 20")) 
Total_bill_with_tip = (tip/100) * bill + bill
No_of_people = int(input("How many people you want to split the bill to?")) #no of people is identified by integer
Each_should_pay = Total_bill_with_tip / No_of_people
final_amount = (round(Each_should_pay , 2))
print(f"Each person should pay:${final_amount}")
