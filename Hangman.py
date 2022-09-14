#Step 2


import random
from hangman_words import word_list
from hangman_art import logo

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for each_letter in chosen_word:
    display += "_"

lives = 6

while '_' in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'You have already guessed {guess}')
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in display:
        print(f'You have already guessed {guess}')

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")


    print(f"{' '.join(display)}")
    if '_' not in display:
        print("You win")
        print(lives)

    print(stages[lives])