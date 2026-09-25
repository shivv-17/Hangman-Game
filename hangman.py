import random

words = {
    "easy": ["apple", "chair", "table", "mango", "shirt"],       # all 5 letters
    "medium": ["hangman", "chicken", "teacher", "kitchen"],      # all 7 letters
    "hard": ["algorithm", "developer", "chocolate"]              # all 9 letters
}

level = input("Choose difficulty (easy/medium/hard): ").lower()
secret_word = random.choice(words[level])

lives = len(secret_word) + 2
guessed_letters = []

while True:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    
    print("\nWord:", display)
    print("Lives remaining:", lives)
    
    if "_" not in display:
        print("\nYou won! The word was:", secret_word)
        break
    
    if lives == 0:
        print("\nYou lost! The word was:", secret_word)
        break
    
    guess = input("Guess a letter, or type the whole word: ").lower()
    
    if len(guess) > 1:
        if guess == secret_word:
            print("\nYou guessed the whole word! You win!")
            break
        else:
            print("That's not the word. You lose a life!")
            lives = lives - 1
            continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)

    lives = lives - 1

    if guess in secret_word:
        print("Correct!")
    else:
        print("Wrong!")
