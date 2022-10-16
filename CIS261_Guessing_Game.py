import random

def display_title():
    print("Guess the number!")
    print()

def play_game(LIMIT):    
    number = random.randint(1, LIMIT)
    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1
    guess = int(input("Your guess: "))

    while (guess != number):
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        guess = int(input("Your guess: "))
    print(f"You guessed it in {count} tries.\n")
     
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        LIMIT = int(input("Enter the limit: "))
        play_game(LIMIT)
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
