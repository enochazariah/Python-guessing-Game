import random
def  guess_game():
    print('welcome to the Quick Guess game!')
    print('I have a number in mind from 1 to 100')
#generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
while True:
    try:

        guess = int(input("make a guess:>  "))
        attempts += 1
        if guess < secret_number:
            print("You guessed too low! Try again.")
        elif guess > secret_number:
            print("You guessed too high! Try again.")
        else:
            print(f"congratulations! You guessed rightly {secret_number} in {attempts} attempts")  
            break
    except ValueError:
        print("please enter a valid number!!!")
if __name__ == '__main__':
    guess_game()






