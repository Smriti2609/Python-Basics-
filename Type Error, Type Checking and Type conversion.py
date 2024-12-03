#type checking
print(type("Hello"))    #string
print(type(1234567890))   #int
print(type(23.44))    #float
print(type([0]))   #list
print(type(True))  #Boolean


#type conversion
int()
float()
str()
bool()
#another program 
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("number of letters in your name: ")) #str
print(type(length_of_name)) #int
print("Number of letters in your name: " + str(length_of_name)) #int

#adding integers 
print(int("123") + int("345"))  #int
print((int(input("Number of letter in your name"))) + int(input("No of letter of your college")))


#type error
print("Number of letter in your name: ") + len(input("No of letter of your college"))
 #it will show type error because we can only concatenate strings (not convert "int") to str.


