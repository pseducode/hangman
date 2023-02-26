#Basic hangman
#uses pygame for screen and for input, using both experimenmt with minviavbble game and
#experiinfinite-game (wordle clone)
import pygame
import sys, os
import hanger
import hanging
import board2
import random
options =["easy","medium","hard"]
stageimages = [] #list of images to load ondices map to number wrong, i.e 0 = just stage,
allowedwrong=0 #number of allowed incorrect guesses before gameover, max =  7 for easy mode (head,body,L-arm,R-arm,R-leg,L-leg, and hat),
#Medium & hard modes only get 6 (not hat)
def texttosurf(text):
    #todo, copy code from hanger class to convert string to blit-able surface
    my_font = pygame.font.SysFont('Comic Sans MS',32)
    txtsurf= my_font.render(text,False,(0, 0, 0))
    return txtsurf
def loadstages():
    global stageimages
    image1=pygame.image.load("stage.png")
    stageimages.append(image1)
    image2=pygame.image.load("stagehead.png")
    stageimages.append(image2)
    image3=pygame.image.load("stageHeadBody.png")
    stageimages.append(image3)
    stageimages.append(pygame.image.load("stageHeadBodyLArm.jpg"))
    stageimages.append(pygame.image.load("stageHeadBodyLArmRarm.png"))
    stageimages.append(pygame.image.load("stageHeadBodyArmsLleg.png"))
    stageimages.append(pygame.image.load("stageHeadBodyArmsLlegs.png"))
    stageimages.append(pygame.image.load("stageHeadBodyArmsLlegsHatSad.png"))
    
    #todo copy code from hanger class to load in stage graphics to global list
def playgame3():
    #actual game, once works/debugged copy/paste to main function/rename
    #first init stuff
    pygame.init()
    size = width, height = 1000, 600
    back = 0, 0,0
    white = 255, 255,255
    screen = pygame.display.set_mode(size)
    loadstages()
    letterin = ""
    modepicked=False
    #first determine difficulty level to set game solution (easy, medium or hard)
    while True: # main game loop
        #while not modepicked:
            #need to set difficulty before starting gameplay
            message =texttosurf("please enter difficulty level for this game (easy medium, or hard): "+letterin)
        #deal with input
        for event in pygame.event.get():
            if event.type ==pygame.QUIT():
                sys.exit()
            if event.type = pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    letterin = letterin[:-1]
                elif ((event.key ==pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN)):
                    #pressed enter/return so validate input
                    if not modepicked: #haven't picked difficulty yet, see if proper diff level
                        if (letterin not in options:
                            message = texttosurf("Sorry, "+letterin+" is not a valid difficul;ty level, please try another: ")
                        else:
                            #entered a valid difficulty level, pick a solution, and init board
                            message = texttosurf("Okay, now picking a solution with difficulty: "+letterin)
                            modepicked=True
                            solution = picksolution(letterin)
                            b=board2.board2(solution)
                    else: #already have a solution check letter in solution etc
                        
                        
                            
                            
                           
                else:
                    letterin+=event.unicode
                    
                    
            
        
    
def playgame2(sol):
    #main game outside of main, for debugging purposes, sol is solution to game, this version uses graphics
    pygame.init()
    #initialize game stuff
    loadstages()
    gameover=False
    b=board2.board2(sol)
    size = width, height = 1000, 600
    black = 0, 0,0
    white = 255, 255,255
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    while not gameover: #main game loop
        stageimage=stageimages[b.howmanywrong()]#stage image to blit to screen
        gameboard = texttosurf(b.boardstatus()) #surface to blit onto screen
        wrongguesses = texttosurf("Wrong guesses: "+b.wrongletters()) #surface of wrong letters to blit onto screen
        """while 1:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT: sys.exit()"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT: sys.exit()
        screen.fill(white )
        screen.blit(stageimage,(width-983, height-400))
        screen.blit(gameboard,(20,height-436))
        screen.blit(wrongguesses,(20,height-50))
        pygame.display.flip()
        clock.tick()
        if('_' not in b.boardstatus()):
            print("Congratulations, you have won the game!")
            gameover=True
            continue
        print("Please enter a guess for letter in solution: ")
        totry=input()
        state = b.makeguess(totry)
        print("currently wrong guesses are: "+b.wrongletters())
        if state:
            print("you made a correct guess!")
        else:
            print("you made ab incorrect guess")
        if(b.howmanywrong() >= allowedwrong):
            print("Sorry, you've had too many incorrect guesses. Game Over!")
            print("FYI, the solution was: "+sol)
            gameover=True
        
            
        
def playgame(sol):
    #main game loop outside of main, for debugging purposes, solution is solution to game
    gameover=False
    b=board2.board2(sol)
    while not gameover:
         print("The boardlooks like this currently: ")
         bstate = b.boardstatus()
         print(bstate)
         if ('_' not in bstate):
              print("Congratulations, you have won the game!")
              gameover=True
              continue
         #print("to debug, bstate is: "+bstate+" and the sol is: "+sol)
         print("Please enter a guess for letter in solution: ")
         totry=input()
         state = b.makeguess(totry)
         if state:
             print("you made a correct guess!")
         else:
              print("you made an incorrect guess!")
         
              #gameover=True
         if(b.howmanywrong() >= allowedwrong):
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
    #start main game loop
    
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
    playgame2(solution)
    

if __name__=="__main__":
    main2()
    
