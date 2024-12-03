#body mass indexb
bmi = 84 / 1.65 ** 2
print(bmi)         #gives output in floating point 
print(int(bmi))    #gives output in integer 
print(round(bmi))  #gives output by rounding off to its nearest value
print(round(bmi , 2))  #gives number of digits you want to print after decimal point


#F-string  {f string combines all kind of datatypes into a string by using f infront of the string.}
score = 0          #int 
height = 1.8       #float
is_winning = True  #bool
print(f"Your score is = {score}, your height is {height}. Your winning condition is {is_winning}")