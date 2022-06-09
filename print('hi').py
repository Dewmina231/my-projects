import random as r
import time as t


yop = True
x = r.randint(1, 99)
guesses = 10




def ag():
    global yop
    global x
    global guesses
    
    rc = int(input("Pick a number between 1-99 (only 10 guesses): "))
    
    if guesses == 1:
        print("you lose the right answer is = " +str(x))
        t.sleep(2)
        yop = False
    
    
    if rc<x:
        print("Too low")
        guesses = guesses-1
        print("Remaining guesses = "+str(guesses))
        
        
    if rc>x:
        print("too high")
        guesses=guesses-1
        print("Remaining guesses = "+str(guesses))
        
        
#refresh if statement
    if rc == x:
        print("you guessed the right answer ")
        yorno= input("Again(Y/N): ")
        if yorno == "y":
            ag()
            guesses=10
        else:
            yop = False
        
    



while yop:
    ag()