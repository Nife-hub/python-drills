import random


def play_game(target=None, max_attempts=3):
    while True:
        if target is not None:
            if type(target) is not int or target < 1 or target > 100:
                print('Invalid target. Target must be a whole number between 1 and 100.')
                return

            number = target
        else:
            number = random.randint(1, 100)

        

        num_of_tries = 0
        won = False

        while num_of_tries < max_attempts:
            try:
                guess = int(input('guess a number between 1 and 100: '))   
            except ValueError:
                print('invalid input. enter a whole number between 1 and 100.')
                continue

            if guess < 1 or guess > 100:
                print('invalid input. enter a whole number between 1 and 100.')
                continue

            num_of_tries += 1

            if guess < number:
                print('too low')
            elif guess > number:
                print('too high')
            else:
                print(f'correct! you got it in {num_of_tries} guesses')
                won = True
                break

        if not won:
            print(f'Max attempts reached! The number was {number}.')

        
        play_again = input('Play again? y/n: ').strip().lower()

        while play_again not in ('y', 'n'):
            print('Invalid option. Please enter y or n.')
            play_again = input('Play again? y/n: ').strip().lower()

        if play_again == 'n':
            print('Thanks for playing!')
            return



# Do not modify below this line
if __name__ == "__main__":
    play_game()
