#letter guessing game 
import random
import string 
def letter_guess_game(attempts = 3):
    secret = random.choice(string.ascii_lowercase)
    print("Welcome to the letter guess game!")
    print(f"You have {attempts} attempts to guess a letter from (a - z). Good luck")

    for remaining in range(attempts, 0, -1):
        guess = input(f"attempts left {remaining}. Enter your guess: ").strip().lower()
        #validate input
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("please enter exactly one letter from a to z.")
            #don't consume an attempt for invalid input; you cam change this if desired 
            continue

        if guess == secret:
            print(f"correct!! you guessed rightly '{secret}'. You won!!!")
            return True
        else:
            #give a simple alphabetical hint
            hint = "after" if guess < secret else "before"
            print(f"wrong. The secret letter comes {hint} '{guess}' alphabetically")

    print(f"You ran out of attempts. The secret letter was '{secret}'. Better luck next time!!")
    return False
if __name__ == "__main__":
    letter_guess_game    
