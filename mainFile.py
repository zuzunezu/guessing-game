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

def main():
    target = choose_random_word(VALID_WORDS)
    guess = input("Enter a four-letter word: ")
    if check_guess(guess, target):
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, the correct word was '{target}'.")


if __name__ == "__main__":
    main()
    