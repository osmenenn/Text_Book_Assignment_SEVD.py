#Ismoil Boboev 
#SEDV TextBook Assignment 4-4.2
#Guess the number game 




import random
##Having fun with this exericise 

print("Good day, Welcome my child this program is very smart it can generate random number, ")
print("in fact it can generate random number faster then you anyways, anywaysss, lets see you loose. ")

#Random number generator 
num = random.randint(1, 10)
guess = None


#setting the condition loop
while guess != num:
    guess = input("throw me a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("Hmmm, not impressed, cgrt! ")
        break
    else:
        print("You thought you could beat a machine? please reserve a seat like everyone else or try again!")