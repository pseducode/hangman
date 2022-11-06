#test for putting the screen, input, and solutrion, thius far all at once
#top left = used/wrong letters
#top right = input area
#bottom left = solution area
#bottom right = stage
import sys,pygame
size = width, height = 1000, 600
black = 0, 0,0
white= 255, 255,255

screen = pygame.display.set_mode(size)

stage = pygame.image.load("stage.png")
base_font = pygame.font.Foint(None, 32)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
solutionsurf = my_font.render('T _ st_ _ _ blah blash _ _ _ ',False,(0, 0,0))

clock = 
