number = "10"
count = 10
print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while count-1 > 0:
    count -= 1
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    guess = input(f"Incorrect. You have {count} guesses left. Try again...")

print(f"You ran out of guesses! The nummber was {number}")