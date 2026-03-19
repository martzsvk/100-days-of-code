import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
lives = 6

print(hangman_art.logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You've already guessed this letter.")
    elif guess in incorrect_letters:
        print("You've already guessed this letter.")
        lives += 1
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            incorrect_letters.append(guess)
            display += "_"


    print("Word to guess: " + display)

    if guess not in  chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    stages = hangman_art.stages
    print(stages[lives])
