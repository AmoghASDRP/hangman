# main: greets user, calls play() to start game
def main():
    # TODO : NEEDS TO BE DONE
    pass


# play: the actual game functionality. uses chooseWord(), 
# guessLetter(), and guessWord() to play the game; also keeps track of lives
# must also be recursive
# Amogh is doing this one
def play():
    word = chooseWord()
    # for word progress bar
    progress = []
    used = []
    lives = 6
    for letter in word:
        progress.append("_")
    while lives > 0 and "_" in progress:
        # display current progress & lives
        print(" ".join(progress)) 
        print("Lives left:", lives)
        guess = input("Guess a letter or guess answer: ").lower().strip()

        if guess == "help":
            displayUsedLetters(used)
            continue

        if guess == "guess answer":
            guess = input("Enter the full word: ")
            
            if guess == word.lower().strip():
                print("Word guessed, you've won!")
                break
            else:
                print("Answer wrong, game over!")
                break
            
            
        else:
            isCorrect = guessLetter(guess, word, progress, used)
            if not isCorrect:
                print("Letter not found!")
                lives -= 1
                
    if "_" not in progress:
        print("Word guessed, you've won!")

    else:
        print("Out of lives, game over!")
    
    replay = input("Play again? (yes/no)").lower().strip()
    while replay != "yes" and replay != "no": 
        replay = input("Invalid input. Play again? (yes/no)").lower().strip()
    if replay == "yes":
        print("New game!")
        play()



# chooseWord: chooses the word. - must be lower case and not have whitespace
# a way: create a list and use random.choice() ?
# should return the word
def chooseWord():
    # TODO: NEEDS TO BE DONE
    pass

# guessLetter: validates input and check if the letter guessed is valid; if so, 
# must be a single alphabetic character
# recursively reprompts in case of user giving invalid input
# if valid, checks if letter is in word
# updates progress and used variable
# returns True if correct, False otherwise

def guessLetter(guess, word, progress, used):
    # TODO: NEEDS TO BE DONE
    pass


# displayUsedLetters: displays the letters used in the correct format as per the project 1 PDF
# bonus function
def displayUsedLetters(used):
    if not used:
        print("Used letters: None")
    else:
        # letters will be sorted in alphabetical order
        letters_sort = sorted(list(used))
        print("Used letters:",", ".join(letters_sort))


if __name__ == "__main__":
    main()


