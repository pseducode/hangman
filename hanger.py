#class in pass 1 to just draw min viable UI
#aka will just be used to load/draw stage + write out solution so far, and guesses
class hanger:
    totalwrong= 0 #number of wong quesses
    board ="" #answerboard thus far
    guesses=[] #list of letters guessed, not in solution
    hangstate="" #image to use for hangman state based on number of wrong guesses
    stageimages = [] #list of images to load ondices map to number wrong, i.e 0 = just stage,
    screen="" #screen things will be displayed on.
    #1 = head, 2 head+body, 3= head+body & l left arm,4 = head+body + both arms
    #5 = head+body+sarms & left leg, 6= heady, body, both arms & both legs, 7 = whole bodyy  + hat
    
    #Class To actually draw hangman & stage, etc.

    def updateboard(self,wrongs,board,guesses):
        pass
        #update boasrd after a guess
    def displayscreen():
        global screen
        
        
    def __init__(self,board,size):
        #first initialize global variables
        global screen
        pygame.init()
        black= 0, 0,0
        white=255, 255,255
        screen=pygame.display.set_mode(size)
        self.totalwrong = 0
        self.board=board,guesses.append(guesses)
    #now initialize all hangingstate images
        image1=pygame.image.load("stage.png")
        stageimages.append(image1)
        image2=pygame.image.load("stagehead.png")
        stageimages.append(image2)
        image3=pygame.image.load("stageHeadBody.png")
        stageimages.append(image3)
        stageimages.append(pygame.image.load("stageHeadBodyLArm.png"))
        stageimages.append(pygame.image.load("stageHeadBodyLArmRarm.png"))
        stageimages.append(pygame.image.load("stageHeadBodyArmsLleg.png"))
        stageimages.append(pygame.image.load("stageHeadBodyArmsLlegs.png"))
        stageimages.append(pygame.image.load("stageHeadBodyArmsLlegsHatSad"))
        #initializeboard now
        my_font = pygame.font.SysFont('Comic Sans MS',30)
        solsurf= my_font.render(board.boardstatus(),False,(0, 0, 0))
         
        
        

