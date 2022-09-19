class hanging:
    import random
    #class to keep track of hangman state (letters guessed, game solution,letters guessed so far and # of wrong guessed)
    #Global variables
    mode=""
    soluition=""
    guesses=[] #list of guesses already tried
    wrongguesses=0 #number of incorrect letters guessed, max =  7 for easy mode (head,body,L-arm,R-arm,R-leg,L-leg, and hat),
    #Medium & hard modes only get 6 (not hat)
    def __init__(self,hardness):
        self.mode =hardness #hardness can be easy, medium or hard, use external .txt wordlists
        #pick random solution, from inuputted difficulty setting
        picksolution()
        
    def gameover(self):
        #True/False as to wether max guesses have been reached, or solution
        return false

    def picksolution():
        #At the astart of the game, pick the solution, based on the difficulty inputted at random, from appropriate wordlist
        print("deciding on a solution, hold on")
        #first determine wordlist to use
        if(mode=="easy"):
            wordchoices = open("easy.txt","r")
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
        
