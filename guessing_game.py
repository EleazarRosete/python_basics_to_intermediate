import random

def try_again():
    while True:
        try:
            choice = int(input("""\nDo you want to try again?
[1. Yes] [2. No]
Enter here: """))
            if choice in [1, 2]:
                return choice
            else:
                print("Please enter 1 or 2 only.")
        except ValueError:
            print("Please enter a valid number.")

def game():
    attempt = 0
    random_number = random.randint(1, 20)
    
    while True:
        if attempt < 3:
            try:
                guess = int(input("Guess the number (1–20): "))
            except ValueError:
                print("❗ Please enter a valid number.")
                continue

            if not 1 <= guess <= 20:
                print("Please enter a number between 1 and 20.")
                attempt += 1
                continue

            if guess > random_number:
                print("Too high!")
            elif guess < random_number:
                print("Too low!")
            else:
                print("🎉 You got it right!")
                break

            attempt += 1
        else:
            print(f"\n💀 Game Over! The correct number was {random_number}")
            break

# Game loop
while True:
    game()
    if try_again() == 2:
        print("\nThanks for playing! See you next time 👋")
        break
