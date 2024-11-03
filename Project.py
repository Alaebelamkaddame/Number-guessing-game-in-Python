import random  # Importing the random module to generate a random number

# Starting message to welcome the player to the game
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

# Generating a random number between 0 and 99 for the player to guess
number_to_guess = random.randrange(100)

# Setting the maximum number of chances a player has to guess the number
chances = 7

# Initializing a counter to keep track of the number of attempts made by the player
guess_counter = 0

# Starting a loop that will continue until the player runs out of chances
while guess_counter < chances:

    # Increment the attempt counter
    guess_counter += 1
    
    # Prompting the player to enter a guess and converting it to an integer
    my_guess = int(input('Please Enter your Guess : '))

    # Checking if the player's guess is correct
    if my_guess == number_to_guess:
        # If correct, display a success message with the correct number and attempt count
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
        break  # Exiting the loop as the game is won

    # Checking if the player has used all chances and still has not guessed the number
    elif guess_counter >= chances and my_guess != number_to_guess:
        # If out of chances, reveal the correct number and display a loss message
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    # Checking if the guessed number is higher than the actual number
    elif my_guess > number_to_guess:
        # Providing feedback that the guess is too high
        print('Your guess is higher ')

    # Checking if the guessed number is lower than the actual number
    elif my_guess < number_to_guess:
        # Providing feedback that the guess is too low
        print('Your guess is lesser')
