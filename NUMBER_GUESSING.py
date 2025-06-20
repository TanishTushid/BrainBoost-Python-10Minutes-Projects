import random

number = random.randint(1,100)
Attempt = 0
print("Guess the number between 1 to 100")

while True:
    guess = int(input("Enter the number -> "))
    Attempt += 1
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too Hight")
    else:
        print(f"Correct!!!...You guessed it in {Attempt} attempts.")
        break
