import random
HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
0   |
    |
    |
   ===''', '''
+---+
0   |
|   |
    |
   ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    === ''', '''
 +---+
 0   |
/|\  |
/    |
    === ''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
#All caps = constant variable, should not be changed later on.

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle mourse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
#The .split() method will place each word in a single list. Words seperated by spaces will be placed in their own index.

def getRandomWordList(wordList):
    #picks a random word from the words list
    rIndex = random.randint(0, len(wordList) - 1)
    return wordList[rIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed Letters: ")
    for letters in missedLetters:
        print(letters, end=" ")
    print()
        

    blanks = "_" * len(secretWord)
    for i in range(len(secretWord)): #replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end=" ")
    

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print("Guess a letter:", end= " ")
        guess = input().lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have aleady guess this letter")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter")
        else:
            return guess

def playAgain():
    #This function return Rrute if the player wants to play again; otherwise, it returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWordList(words)
gameIsDone = False

while True: 
    #Display the board
    displayBoard(missedLetters, correctLetters, secretWord)

    #Allows the player to make a guess.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord: 
        correctLetters += guess

    #Check if player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False

        if foundAllLetters:
            print("Yes! The word is " + secretWord + "! You won!")
            gameIsDone = True
    else:
         missedLetters += guess
    
    #Check if the player has lost.
    if len(missedLetters) == len(HANGMAN_PICS) -1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print("You have run out of guesses! \n" + "The word was: " + secretWord)
        gameIsDone = True

    if gameIsDone: 
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWordList(words)
        else:
            break #ends game

    


    

    



    


