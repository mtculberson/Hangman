from string import ascii_lowercase
import random

WORDLIST = 'wordlist.txt'

def get_random_word(word_length):
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) != word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word

def get_num_attempts():
    while True:
        num_attempts = input(
            'How many incorrect tries should we have? (1 to 25) ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print('{0} isnt between 1 and 25'.format(num_attempts))
        except ValueError:
            print('{0} is not a number'.format(
                num_attempts))

def get_word_length():
    while True:
        word_length = input(
            'What word length should we have? (4-16) ')
        try:
            word_length = int(word_length)
            if 4 <= word_length <= 16:
                return word_length
            else:
                print('{0} is not a number between 4 and 16'.format(word_length))
        except ValueError:
            print('{0} is not a number'.format(
                word_length))


def get_word_displayed(word, idxs):
    displayed_word = ''.join(
        [letter if idxs[i] else '_' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single letter'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_hangman():
    """Actual hangman activity."""
    print('Lets play Hangman!')
    attempts_remaining = get_num_attempts()
    word_length = get_word_length()

    word = get_random_word(word_length)
    print()
    
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    solved = False

    while attempts_remaining > 0 and not solved:
        print('Word: {0}'.format(get_word_displayed(word, idxs)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previously Guessed Letters: {0}'.format(' '.join(wrong_letters)))

        next_letter = get_next_letter(remaining_letters)

        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))

            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{0} is NOT in the word!'.format(next_letter))

            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        if False not in idxs:
            solved = True
        print()

    print('The correct word is {0}'.format(word))

    if solved:
        print('Congrats! You guessed the word correctly!')
    else:
        print('Try harder next time!')

    try_again = input('Would you like to play again? (y/n) ')
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while play_hangman():
        print()

