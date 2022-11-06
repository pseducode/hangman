#class in pass 1 to just draw min viable UI
#aka will just be used to load/draw stage + write out solution so far, and guesses
class hanger:
    totalwrong= 0 #number of wong quesses
    board ="" #answerboard thus far
    guesses=[] #list of letters guessed, not in solution
    hangstate="" #image to use for hangman state based on number of wrong guesses
    
    #Class To actually draw hangman & stage, etc.

    def updateboard(self,wrongs,board,guesses):
        pass
        #update boasrd after a guess
    def displayscreen():
        print("sdome bs placeholder")
        
    def __init__(self,board,guesses):
        #first initialize global variables
        self.totalwrong = 0
        self.board=board,guesses.append(guesses)
        #now initialize all hangingstate images
        

