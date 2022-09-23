import hanging
def main():
    print("Hello Mr. Hangman player!")
    game = hanging.hanging("medium")
    game.picksolution()
    while (not game.gameover()):
        print("The board looks like this:\n")
        game.drawsol()
        print("What is your guess?")
        guess=input()
        game.makeguess(guess)
        
    
if __name__=="__main__":
    main()
    
   
