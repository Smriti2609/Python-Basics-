#python has a lot of built in function and we have already used some of them .for example: int(), len(), print() and so on.
#we can identify a function as function has paranthesis in it.()

#if we want to create our own function, we start we the a keyword def functionname():
print("Hello")
num_char = len("Hello")
print(num_char)
def my_function():  #defining own function.
    print("Hello")
    print("Bye")
my_function()   #calling the function is necessary to get the output of the above code.


#so the way of defining the function in python is simple:
# def my_function():
    #Do this 
    #then do this 
    #Finally do this 
#calling function (calling function is necessary at last because once the computer goes through the calling
#function it will know that it has to carry out all the action mentioned inside the defined function.)



#for a perfect example of defining or calling python functions, we can visit the page mentioned here and 
#see how function works with the basic example of a simple game.  
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json   


#you can also try a game of accomplishing the goal by a robot in Reeborg's World followed by this link
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#you can use this code to complete the challenge.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(0, 6):
#     jump()