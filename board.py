#Class to keep track of the hangmsn board

class board:
    solution = "" #solution player is trying to guess
    numwrongguesses=-1
    guesses = [] #All letters guessed so far
    nonlets=('.',',','?',',','!')#non-letter characters in solution, possible
    won= False
    board = "" # What the board of placeholders +right guesses
    def gameover (self,allowedwrong):
        print ("in game over function!")
        if self.won: #guesed all letters iin solution, game over but won. say so
            print("Congratulations! You won the game!")
        print("recorded wrongs is: "+str(self.numwrongguesses))
        print("acceptable wrong is: "+str(allowedwrong))
        return self.numwrongguesses <allowedwrong or self.won
    def makeguess(self,guess):
        self.guesses.append(guess.lower())
        #return true is guess is in solution, false otherwise
        if guess.lower() in self.solution.lower():
            print("You guessed a correct letter!")
            return False
        else:
            print("Your guess of: "+guess+" is not in the solution, sorry!")
            self.numwrongguesses+=1
            return True

    """def drawboard(self):
        todraw = ""
        for letter in self.solution:
            if (letter.lower() in self.guesses):
                todraw+=letter
            elif (letter in self.nonlets):
                todraw+=letter
            else:
                todraw+="_ "
            print("The current board is: ")
            print(todraw)"""
    def drawboard(self):
        todraw = ""
        for letter in self.solution:
            if ((letter.lower() not in self.guesses) and (letter not in self.nonlets)):
                todraw+="_ "
            elif letter in self.nonlets:
                todraw+=letter
                todraw+=" "
            else:
                todraw+=letter
        print("The current board is: ")
        print(todraw)
        if(todraw.lower()==self.solution.lower()):
            self.won=True
        print("The value of won, is:"+str(self.won))
        print()
                           
    def __init__(self,answer):
        self.solution =answer
        self.guesses.append(" ")
        self.numwrongguesses=0
        
