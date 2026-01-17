import random

print("Welcome to the Random Number Guessing Game!")
print("I have selected a random number between 1 and 100.")
print("Try to guess the number!")
answer = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Please enter an integer between 1 and 100.")
            continue
        if guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Correct! Guessed in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a number.")

if attempts >= max_attempts:
    print(f"Game over! Answer was {answer}.")

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == answer:
        print("Correct!")
    else:
        print("Incorrect!")
