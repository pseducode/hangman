#Class to keep track of the hangmsn board

class board:
    solution = "" #solution player is trying to guess
    guesses = [] #All letters guessed so far
    board = "" # What the board of placeholders +right guesses
    def makeguess(self,guess):
        #return true is guess is in solution, false otherwise
        return guess.lower in solution
    def __init__(self,answer):
        self.solution =answer.lower() #set board's solution
        
