number = "10"

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while 1 == 1:
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    guess = input("Try again...")