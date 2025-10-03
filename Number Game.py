import random
print("\nYou have 5 chances to guess the number between 1 and 100. Let's Start!") 
n=random.randrange(1,100)
chances=5
gc=0 #Guess counter
while gc<chances:
    gc+=1
    guess=int(input("Enter any number: "))
    if guess==n:
        print("You guessed it right!!")
        break
    elif gc>=chances and guess!=n:
        print(f"Sorry! Your chances finish. The number was {n}.")
    elif guess>n:
        print("Too high")
    else:
        print("Too low")
