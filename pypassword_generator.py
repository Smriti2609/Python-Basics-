import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '?']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#Easy level
# password = " "


# for char in range(0, nr_letters):
#     #1 - 4 letters will be included in our pw.
#     password += random.choice(letters)
    
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# print(password)


#hard level

password_list = []
for char in range(0, nr_letters):
    password_list += random.choice(letters)
    
for char in range(0, nr_symbols):
    password_list += random.choice(symbols)#its like password_list = password_list + random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list) #shuffle is the function that is used to create or reorder the sequence in the list.
print(password_list)

#turning it back into string as upto this step, the password is generated in list form.
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
    

