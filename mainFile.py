import random
#Define dictionary of the valid four letter words
#(perfect match)

VALID_WORDS = [
    "able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"
]

def choose_random_word(word_list):
    #randomly chooses and returns a word from the list
    return random.choice(word_list)

def check_guess(guess, target_word):
    return guess.lower() == target_word.lower()

def run_game():
    print("Welcome to the Word Guessing Game!")
    print("You have 5 turns to guess the word. Good luck!\n")

    target = choose_random_word(VALID_WORDS)
    attempts_left = 5

    while attempts_left > 0:
        guess = input(f"Enter your guess ({attempts_left} attempts left): ")
        #check if the guess is empty or not in the list 
        if guess.strip() not in VALID_WORDS:
            print("Invalid guess. Please enter a valid four-letter word, or is empty. Try again\n")
            continue
        
        
        if check_guess(guess, target):
            print("Congratulations! You've guessed the word!")
            return #exit the function if user guessed it correcrtly
        else:
            print("Incorrect guess. Try again.")
            attempts_left -= 1
    print(f"Sorry, you've run out of attempts. The word was '{target}'.")
    


def main():
    
    '''
    target = choose_random_word(VALID_WORDS)
    guess = input("Enter a four-letter word: ")
    if check_guess(guess, target):
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, the correct word was '{target}'.")
    '''
    run_game()


if __name__ == "__main__":
    main()
