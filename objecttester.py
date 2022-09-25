#scrap python file to test out individual objects
import board
def main():
    over = False
    b = board.board("testing")
    while not over:
        print("please input your guess of solution")
        guess=input()
        b.makeguess(guess)
        over = b.gameover(6)
        print ("The value of over is: "+str(over))
    
if __name__=="__main__":
    main()
