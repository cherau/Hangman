# hangman game

import random

from words import word_list 

def body(val):
    left = ["""             
              _____________
             |             |
             |             O
             |            /|\\
             |            / \\
            ____     """,
            """            
              _____________
             |             |
             |             O
             |            /|\\
             |            / 
            ___    """, 
             """             
              _____________
             |             |
             |             O
             |            /|\\
             |              
            ___   """,
             """              
              _____________
             |             |
             |             O
             |            /|
             |
            ___   """,
             """              
              _____________
             |             |
             |             O
             |            /
             |     
            ___        """,
             """             
              _____________
             |             |
             |             O
             |            
             | 
            ___           """,
             """
              _____________
             |             |
             |             
             |            
             | 
            ___            """]
    print(left[val])

if __name__=='__main__':

    word = random.choice(word_list)
    guessed = list('_' * len(word))
    chances = 6
    print("\n \t \t \t \t \t \t HANGMAN \nNumber of letters :", len(word))
    while (True):
        guess = input('\nEnter a letter : ')
        if( guess in word ):
            for i in range (len(word)):
                if( word[i] == guess ):
                    guessed[i] = guess
            print("".join(guessed))
            
            if( "".join(guessed)==word ):
                print("\nYOU WIN !")
                break
        else:
            print(guess,' is not present in the Word')
            print("".join(guessed))
            chances-= 1 

        body(chances)

        if( chances==False ):
            print("\n GAME OVER ! \n The word was",word)
            break   