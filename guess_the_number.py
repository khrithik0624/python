import random

def guess_user(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input('Make a guess: '))
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")

    print(f"You guessed the number {guess} correctly!!!")

def guess_comp(x):
    high=x
    low=1
    feedback=''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"The number is {guess} ???  (H) for too high , (L) for too low, (C) for correct guess!: ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    
    print(f"The computer guessed your number {guess} correctly!!!!")

x=int(input("Set the range: "))
guess_user(x)
guess_comp(x)