 elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You ran out of lives. The word was", word)
    else:
        print("Congratulations! You guessed the word:", word)

if __name__ == '__main__':
    hangman()