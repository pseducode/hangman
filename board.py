#Class to keep track of the hangmsn board

class board:
    solution = "" #solution player is trying to guess
    numwrongguesses=-1
    guesses = [] #All letters guessed so far
    nonlets=('.',',','?','!')#non-letter characters in solution, possible
    board = "" # What the board of placeholders +right guesses
    def gameover (self,allowedwrong):
        print ("in game over function!")
        print("recorded wrongs is: "+str(self.numwrongguesses))
        print("acceptable wrong is: "+str(allowedwrong))
        return not self.numwrongguesses <allowedwrong
    def makeguess(self,guess):
        self.guesses.append(guess)
        #return true is guess is in solution, false otherwise
        if guess.lower() in self.solution.lower():
            print("You guessed a correct letter!")
            return True
        else:
            print("Your guess of: "+guess+"is niot in the solution, sorry!")
            self.numwrongguesses+=1
            return False

    def __init__(self,answer):
        self.solution =answer
        self.numwrongguesses=0
        
