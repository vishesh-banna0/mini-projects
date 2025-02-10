import random

ai_choice = random.randint(1, 100)
print("Game is ON")
print("I have chosen a number between 1 and 100.")
print("Your task is to guess the number correctly.")

while True:
    try:
        user_guess = int(input("Enter Your Guess: "))

        if user_guess not in range(1, 101):
            print("You are out of bounds! Guess between 1 and 100.")
            continue  # Prevent further processing

        if ai_choice == user_guess:
            print("Bingo!! That's the number!")
            break

        difference = ai_choice - user_guess

        if difference in range(1, 4):
            print("You are very close! Go slightly up.")
        elif difference in range(-3, 0):
            print("You are very close! Go slightly down.")
        elif difference < 0:
            print("Too high! Go lower.")
        else:
            print("Too low! Go higher.")

    except ValueError:
        print("Invalid input! Please enter a number.")
