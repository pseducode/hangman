 #more basic board, removing game logic, just tracks solution, and guesses
class board2:
    solution="" #solution player is trying to guess
    numwrong=0 #number of incorrect guesses a player has made
    guesses=[] #all guesses made so far
    wrongguess=[] #incorrect guesses
    nonlets=('.',',','?',',', ' ','!')#non-letter characters in solution, possible
    won=False #guessed all letters in solutyion or not

    def __init__(self,answer):
        self.solution=answer[:-1]
        self.guesses=[]
        self.numwrong=0
        self.wrongguess=[]

    def makeguess(self, guess):
        self.guesses.append(guess.lower())
        if guess.lower() in self.solution:
            return True
        else:
            self.numwrong+=1
            #self.wrongguess.append(guess)
            return False
    def howmanywrong(self):
        #return number of wrong guesses made
        return self.numwrong
    def wrongletters():
        #return list of all wrongly guessed letters
        return self.wrongguess
    def boardstatus(self): #returmn solution so far
        todraw = ""
        for letter in self.solution:
            if((letter.lower() not in self.guesses) and (letter not in self.nonlets)):
                todraw+="_ "
            elif letter in self.nonlets:
                todraw+=letter
            else:
                todraw+=letter
        return todraw
    
        
        
        


    
