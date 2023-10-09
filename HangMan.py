import random

WORDLIST_FILENAME = "words.txt"


def load_words(WORDLIST_FILENAME):
    wordlist = list()
    with open(WORDLIST_FILENAME) as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
    return wordlist


wordlist = load_words('words.txt')


def choose_word(wordlist):
    return random.choice(wordlist)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()


def play_hangman():
    print("Welcome to Hangman!\n")

    words = load_words(WORDLIST_FILENAME)
    word = choose_word(words)

    guessed_letters = set()
    remaining_chances = 10
    guessed_word = display_word(word, guessed_letters)

    correct = ''

    while len(correct) < len(word) and remaining_chances > 0:
        print(guessed_word)
        wrong_guesses = sorted(guessed_letters - set(word))
        print("Guessed letters: " + ", ".join(wrong_guesses))
        print("Chances Remaining: " + str(remaining_chances))

        guess = input("Your guess (letters only): ").strip().lower()

        if not is_valid_guess(guess):
            print("Not a valid character. Please enter a letter .")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
        elif guess in word:
            guessed_letters.add(guess)
            guessed_word = display_word(word, guessed_letters)
            for letter in word:
                if guess == letter:
                    correct = correct + letter
        else:
            guessed_letters.add(guess)
            remaining_chances -= 1
            print("This character is not present in the word.")

    if len(correct) == len(word):
        print("Congratulations, you guessed the word: " + word)
    else:
        print("You ran out of chances! The word was: " + word)


if __name__ == '__main__':
    play_hangman()
