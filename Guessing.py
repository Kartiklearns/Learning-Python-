secret_word = " Kartik "
guess = " "

while guess != secret_word:
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("Congratulations! You've guessed the secret word.")
    else:
        print("Incorrect guess. Try again!")