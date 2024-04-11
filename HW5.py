#File: HW5.py
#Author: Max Allen
#UT EID: mca2773
#Course: CS303E
#I will be creating a hangman game.

import random

def load_words(filename):
    """
    Creates a list of words from the file contents

    Parameters
    ----------
    filename : str
        Name of the file to be processed, contains a single word on each line
    
    Returns
    -------
    word_list : list or str
        List of words, each element is a word from the file
    """
    word_list = []
    try:
        file = open(filename, "r")
        for line in file:
            word = line.strip()
            word_list.append(word)
        file.close()
    except FileNotFoundError:
        print("File not found. Please ensure that 'words.txt' is in the same folder.")
    return word_list

def is_contained(lst, item):
    """
    Checks to see if a given element is in a given list

    Parameters
    ----------
    lst : list
        A list of any kind to be checked
    item :
        A value of any kind to be checked if its in lst

    Returns
    -------
    True : bool
        if elem is in lst
    False : bool
        if elem is not in lst
    """
    for elem in lst:
        if elem == item:
            return True
    return False

def play_hangman():
    """
    Plays a game of hangman with the user

    Asks the user to enter a letter and checks to see
    if that letter is in a randomly chosen word. The
    function then creates a slate to represent the
    word, replacing non-guessed letters with under-
    scores. The user gets 8 guesses.
    
    """
    # This is the setup for the game.
    word = random.choice(load_words('words.txt'))
    print("Let's play hangman!")
    slate = (len(word)*"-")
    print(slate)
    tries = 8
    guesses = []
    new_slate = ""
    # This whole while loop is the game and won't stop until the user
    #   wins or loses
    
    while str.isalpha(slate) == False and tries != 0:
        letter = str.lower(str(input("Guess a letter: ")))
        while is_contained(guesses, letter):
            print(f"You've already guessed {letter}")
            letter = str.lower(input("Guess a letter: "))
        while str.isalpha(letter) == False or len(letter) != 1:
            print("That is not a letter. Enter a letter. ")
            letter = str.lower(input("Guess a letter: "))
        # Checking if the guess is in the word
        # while also adding previously correct letters
        # to the slate
        
        for i in range(len(word)):
            if letter == word[i]:
                new_slate += letter
                tries += 1
            elif str.isalpha(slate[i]):
                new_slate += slate[i]
            else:
                new_slate += "-"
        # Resetting for next loop
        
        slate = new_slate
        new_slate = ""
        print(slate)
        tries -= 1
        guesses.append(letter)
        if str.isalpha(slate) == False:
            print(f"You have {tries} tries remaining.")

    # Now the game is over I check if they won or lost
    
    if str.isalpha(slate):
        print("You win!")
    else:
        print(f"You lose. The word was {word}.")
    

def main():
    play_hangman()

if __name__ == '__main__':
    main()
