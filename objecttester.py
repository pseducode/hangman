#scrap python file to test out individual objects
import board
def main():
    over = False
    b = board.board("Test")
    while not over:
        b.drawboard()
        if b.won:
            print ("you won! this is in main game loop btw!")
            break
        print("please input your guess of solution")
        guess=input()
        b.makeguess(guess.lower())
        over = b.gameover(6)
        print ("The value of over is: "+str(over))
    
if __name__=="__main__":
    main()
