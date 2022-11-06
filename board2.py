#more basic board, removing game logic, just tracks solution, and guesses
class board2:
    solution="" #solution player is trying to guess
    numwrong=0 #number of incorrect guesses a player has made
    guesses=[] #all guesses made so far
    wrongguess=[] #incorrect guesses
    nonlets=('.',',','?',',','!')#non-letter characters in solution, possible
    won=False #guessed all letters in solutyion or not

    def __init__(self,answer):
        self.solution=answer
        self.guesses=[]
        self.numwrong=0
        self.wrongguess=[]

    def makeguess(guess):
        pass
    def returnboard(): #returmn solution so far
        pass
        


    
