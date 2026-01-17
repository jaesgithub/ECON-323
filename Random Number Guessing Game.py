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
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() == "y":
                answer = random.randint(1, 100)
                attempts = 0
            else:
                break
                print("Thanks for playing!")
            break
    except ValueError:
        print("Please enter a number.")

if attempts >= max_attempts:
    print(f"Game over! Answer was {answer}.")
