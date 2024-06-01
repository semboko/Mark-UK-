from random import choice

words = list(("silver", "gold", "pizza"))

secret_word = choice(words)
lives = 9
correct_letters = set()


def hide_letters(word):
    result = ""
    for letter in word:
        if letter in correct_letters:
            result += letter
        else:
            result += "*"
    return result


def print_lives_info(lives):
    result = ""
    for i in range(lives):
        result += "❤️"
    print("You have", result)


while True:
    print("The word is: ", hide_letters(secret_word))
    print_lives_info(lives)
    print("Guess a letter from the word:")
    
    new_letter = input()
    
    if new_letter == "!":
        print("Buy! See you again!")
        exit()
    
    if len(new_letter) > 1:
        print("Only one letter is accepted")
        continue
    
    if lives <= 0:
        print("Game over")
        exit()
    
    if new_letter not in secret_word:
        print("Incorrect! Try again...")
        lives = lives - 1
        continue

    correct_letters.add(new_letter)
    print("The letter is correct! Keep guessing...")
    
    if set(secret_word) == correct_letters:
        print("Congradulations! You guessed the word!")
        exit()
    