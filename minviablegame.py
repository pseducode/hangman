#Basic hangman
#uses pygame for screen, but console for input
import pygame
import sys, os
import hanger
import hanging
import board2
import random
options =["easy","medium","hard"]
allowedwrong=0 #number of allowed incorrect guesses before gameover, max =  7 for easy mode (head,body,L-arm,R-arm,R-leg,L-leg, and hat),
#Medium & hard modes only get 6 (not hat)

def playgame(sol):
    #main game loop outside of main, for debugging purposes, solution is solution to game
    gameover=False
    b=board2.board2(sol)
    while not gameover:
         print("The boardlooks like this currently: ")
         bstate = b.boardstatus()
         print(bstate)
         print("to debug, bstate is: "+bstate+" and the sol is: "+sol)
         print("Please enter a guess for letter in solution: ")
         totry=input()
         state = b.makeguess(totry)
         if state:
             print("you made a correct guess!")
         else:
              print("you made an incorrect guess!")
         if (bstate==sol):
              print("Congratulations, you have won the game!")
              gameover=True
         elif(b.howmanywrong() >= allowedwrong):
            print("Sorry, you've had to many incorrect guesseses. Game Over!")
            print("FYI, the solution was: "+sol)
            gameover=True
         
        
        
def picksolution(mode):
    global allowedwrong
    print("selecting a solution")
    fname = mode + ".txt" #file name of solution list to open
    wordchoices = open(fname, "r")
    wordlist = wordchoices.readlines()
    numoptions =len(wordlist)
    #determing number of allowed incorrectguesses based on doifficulty selecxted.
    if mode =="easy":
        allowedwrong=7
    else:
        allowedwrong=6
    return(wordlist[random.randint(0,numoptions-1)])
def main2():
    pygame.init()
    modepicked=False
    print("Wlcome to my hangman game!")
    while not modepicked:
        #print("testing!")
        
        print("How difficult do you want the game to be? (easy, medium or hard)?")
        level=input()
        if level not in options:
            print("error! "+level+"is not a valid difficulty option!")
        else:
            modepicked=True
            print("Alrighty, you've selected the difficulty of: "+level)
    solution = picksolution(level)
    print("alrighty then, given your chosen difficulty, the solution I've picked is:\n"+solution)
    print ("The number of possible wrong guiesses you havem given difficulty selected is: "+str(allowedwrong))
    playgame(solution)
    

if __name__=="__main__":
    main2()
    
