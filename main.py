# main: greets user, calls play() to start game
def main():
    pass

# play: the actual game functionality. uses chooseWord(), 
# guessLetter(), and guessWord() to play the game; also keeps track of lives
# must also be recursive
def play():
    lives = 6

# chooseWord: chooses the word. 
# one way to do this is here: https://pypi.org/project/random_word ? 
# another way: create a list and use random.choice() ?
def chooseWord():
    pass

# guessLetter: validates input and check if the letter guessed is valid; if so, 
# checks whether it's in the word
# should probably return true or false
def guessLetter():
    pass

# guessWord: checks whether the word guessed is the word
# should probably return true or false
def guessWord():
    pass


if __name__ == "__main__":
    main()


