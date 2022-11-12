#Basic hangman
#uses pygame for screen, but console for input
import pygame
import sys, os
import hanger
import hanging
import board2
import random
options =["easy","medium","hard"]
allowedwrong=0

def picksolution(mode):
    print("selecting a solution")
    fname = mode + ".txt" #file name of solution list to open
    wordchoices = open(fname, "r")
    wordlist = wordchoices.readlines()
    numoptions =len(wordlist)
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
    

if __name__=="__main__":
    main2()
    
