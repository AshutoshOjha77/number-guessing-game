import random
n = random.randint(1,100)
a = int(input("Enter your guess number:-  "))
t = 0
while n!=a:

    if n > a:
        print ("The number is higher than your guess number")
    elif n < a:
        print("The number is lower than your guess number")  
    a= (int(input("Guess again:- ")))
    t += 1
   
print("You guessed it!!!")   
print(n)   
print(f"You guessed it after {t} tries")
 