#script to test out hanger object for graphics, etc
import pygame
import sys,os
import hanger
import board2


def main():
    b=board2.board2("TEST")
    h=hanger.hanger(b,(1000,600))
    #refactor hanger class to accept screen object from get-go, and just blit things onto it
    while 1:
        screen = h.displayscreen()
        screen.flip()
        
    
    
    
if __name__=="__main__":
    main()
