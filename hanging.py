import random
class hanging:
    #class to keep track of hangman state (letters guessed, game solution,letters guessed so far and # of wrong guessed)
    #Global variables
    mode=""
    soluition=""
    wrongguesses=[] #list of guesses already tried, and are wrong
    right guesses=[] #list of guesses, in the actual solution
    numwrongguesses=0 #number of incorrect letters guessed, max =  7 for easy mode (head,body,L-arm,R-arm,R-leg,L-leg, and hat),
    #Medium & hard modes only get 6 (not hat)
    def __init__(self,hardness):
        self.mode =hardness #hardness can be easy, medium or hard, use external .txt wordlists
        #pick random solution, from inuputted difficulty setting
        print("deciding on a solution, hold on a minute")
        #if (mode=="easy"):
            #wordchoices
        #picksolution()
        

    def makeguess(self,guess):
        if (guess not in self.solution):
            guesses.append(guess)
            wrongguesses+=1
            return False
        else:
            
        
        
    def gameover(self):
        #True/False as to wether max guesses have been reached, or solution met
        return wrongguesses<6
        return false

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
        
