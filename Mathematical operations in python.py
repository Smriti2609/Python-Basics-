print("My age:" + str(12)) 
print(123 + 456)   #addition
print(7 - 3)       #subtraction
print(3 * 2)       #multiplication
print(6 / 3)       #division (it provides output on floating number by default)
print(5 / 3)       #division
print(5 // 3)      #division(provides output in integer)
print(2 ** 3)      #gives access to exponent i.e. (2)^3
print(2 ** 2)      #exponent


#PEMDAS (order of priorities) parentheses,Exponents,Multiplication/Division,Addition/Subtraction
print(3 * 3 + 3 / 3 - 3)  #[left to right calculation takes place if the signs with equal priorities occurs. ]
 
print(3 * (3 + 3) / 3 - 3) #adding paranthesis makes the addition operation priority high giving output 3 at last.


#BMI calculator The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.Formula to calculate:bmi is equal to the person's weight divided by the person's height squared.Convert it into code on line 25.

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height ** 2))

print(bmi)