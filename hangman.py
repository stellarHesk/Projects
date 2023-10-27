'''
Game of hangman
'''
import random


FILE_NAME = 'hangman_phrases.txt'
HANG_MAN = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

,
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]
def read_contents(filename: str) -> list:
    '''
    Reads the list of words from the file
    '''
    with open(filename, 'r') as file:
        contents = file.readlines()
    for index in range(len(contents)):
        contents[index] = contents[index].strip()
        contents[index] = contents[index].upper()
    return contents


def display_hang_man(stage: int) -> None:
    '''
    Display the hangman diagram based on which stage it is.
    '''
    print(HANG_MAN[stage])


def make_lines(target_word: str) -> str:
    '''
    Creates and intializes the empty lines for the game
    '''
    lines_list = []
    for char in target_word:
        if str.isalpha(char):
            lines_list.append("_")
        else:
            lines_list.append(char)
    lines_str = ''.join(lines_list)
    return lines_str


def update_lines(lines: str, word: str, input_letter: str) -> str:
    '''
    Updates the blank spaces based on the user's guess
    '''
    letter_indexes = []
    lines_list = [x for x in lines]
    for index in range(len(word)):
        if word[index] == input_letter:
            letter_indexes.append(index)
    for item in letter_indexes:
        lines_list[item] = input_letter
    new_lines = ''.join(lines_list)
    return new_lines


def main() -> None:
    wrong_guesses = []
    words_list = read_contents(FILE_NAME)
    word_selection = random.choice(words_list)
    lines = make_lines(word_selection)
    game_stage = 0
    last_stage = 6
    word_guess = ''
    while game_stage < last_stage and lines != word_selection:
        display_hang_man(game_stage)
        print(lines)
        print(f"Wrong guesses: {','.join(wrong_guesses)}")
        guess = input("What is your guess? Or type '*' to guess the whole phrase: ").upper()
        if guess == '*':
            word_guess = input("Guess the full phrase!: ").upper()
            break

        while guess in wrong_guesses or guess in lines:
            guess = input("Please enter guess you haven't yet entered!: ").upper()
        if guess not in word_selection:
            wrong_guesses.append(guess)
            game_stage += 1
        else:
            lines = update_lines(lines, word_selection, guess)
    if lines == word_selection:
        display_hang_man(game_stage)
        print(lines)
        print("You won! Congratulations!")
    elif word_guess == word_selection:
        display_hang_man(game_stage)
        print(word_selection)
        print("You won! Congratulations!")
    else:
        display_hang_man(6)
        print("Unfortunately, you lost!")
    
        
if __name__ == "__main__":
    main()

