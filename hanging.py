import random
class hanging:
    #class to keep track of hangman state (letters guessed, game solution,letters guessed so far and # of wrong guessed)
    #Global variables
    mode=""
    solution=""
    wrongguesses=[] #list of guesses already tried, and are wrong
    rightguesses=[] #list of guesses, in the actual solution
    numwrongguesses=0 #number of incorrect letters guessed, max =  7 for easy mode (head,body,L-arm,R-arm,R-leg,L-leg, and hat),
    #Medium & hard modes only get 6 (not hat)
    nonlets=('.',',','?','!')#non-letter characters in solution, possible
    def __init__(self,hardness):
        self.mode =hardness #hardness can be easy, medium or hard, use external .txt wordlists
        #pick random solution, from inuputted difficulty setting
        print("deciding on a solution, hold on a minute")
        #if (mode=="easy"):
            #wordchoices
        #picksolution()
        

    def makeguess(self,guess):
        if (guess.lower() not in self.solution.lower()):
            self. wrongguesses.append(guess)
            numwrongguesses+=1
            print("your guess of: "+guess+"Was incorrect, sorry!")
        else:
            rightguesses.append(guess)
            
        
        
    def drawsol(self):
        board = ""
        for letter in self.solution:
            if(letter.lower() in rightguess):
                board+=letter
            elif(letter in nonlets):
                board+=letter
            else:
                board+="_"
            print(board)
        
    def gameover(self):
        #True/False as to wether max guesses have been reached, or solution met
        if(self.numwrongguesses<6):
            return False
        else:
            return True

    def picksolution(self):
        #At the astart of the game, pick the solution, based on the difficulty inputted at random, from appropriate wordlist
        print("deciding on a solution, hold on")
        #first determine wordlist to use
        if(self.mode=="easy"):
            wordchoices = open("easy.txt","r")
        elif (self.mode=="medium"):
            wordchoices = open("medium.txt","r")    
        else:
            wordchoices= open("hard.txt","r")
        #next determine length of wordlist and pick one of the solutions
        wordlist = wordchoices.readlines()
        numoptions = len(wordlist)
        solution = wordlist[random.randint(0,numoptions-1)]
        print("Picked the solution")
        print(solution)
        #remove newline from solution.
        solution = solution.replace('\n','')
        wordchoices.close()
        
