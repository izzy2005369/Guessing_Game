import random


def main():
    guess = random.choice(range(51))

    over = 0
    limit = 10
    user = ""
    out_of_guesses = False
    points = 10
    total_scores = points
    try:
        while user != guess and not out_of_guesses:
            if over < limit:
                print(f'You have {points} chances left')
                user = int(input('Guess a number from the range of 0 - 50\n> '))
                points -= 1
                over += 1
            else:
                out_of_guesses = True

            # To give the player a hint
            if user > guess:
                print("\nThe number is lower than what you guessed, try again")
            elif user < guess:
                print("\nThe number is greater than what you guessed, try again")

        # if the player is out of guess
        if out_of_guesses:
            print('You have 0 score, You lose!.')
        else:  # The else statement is when the player guess right
            print('\nYou get the number correctly, You win!.')
            print(f'It took you {over} guesses and your total scores is {points + 1} / {total_scores}')  # This is to print the number of guesses before getting it right,and also print out the player's scores

    except ValueError:
        print("You inputted wrongly")
    except KeyboardInterrupt:
        print("\nYou cancelled the program")


# calling the function
if __name__=="__main__":
    main()
