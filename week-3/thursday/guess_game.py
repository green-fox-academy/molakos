from random import randint

def get_integer():
    number = int(input("Enter an integer (0-10): "))
    return number

number_to_guess = randint(0,10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()

    except ValueError:
        print("You entered a wrong value.")

    else:
        if guess == number_to_guess:
            print("You won! You are a rockstar!!! #YOLO #SWAG.")
            break

        elif guess > number_to_guess:
            print("My number is smaller.")
            number_of_guesses -= 1
            print("Remaining guesses: ",number_of_guesses)

        elif guess < number_to_guess:
            print("My number is bigger.")
            number_of_guesses -= 1
            print("Remaining guesses: ", number_of_guesses)

if number_of_guesses == 0:
    print("Game over! You are a looser!")
