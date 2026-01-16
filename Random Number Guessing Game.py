import random

n = random.randint(1, 100)
i = random.randint(1, 100)

print("Welcome to the Random Number Guessing Game!")
print("I have selected a random number between 1 and 100.")
print("Try to guess the number!")

while n != i:
    print(n)
    n = random.randint(1, 100)