number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while 1 == 1:
    if guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    if guess > number:
        guess = input("Your guess is too high. Try again...")
    else:
        guess = input("Your guess is too low. Try again...")