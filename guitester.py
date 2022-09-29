import sys,pygame
pygame.init()
size = width, height = 1000, 600
black= 0, 0,0
white=255, 255,255


screen = pygame.display.set_mode(size)

stage = pygame.image.load("stage.png")
stagerect = stage.get_rect()
my_font = pygame.font.SysFont('Comic Sans MS',30)
txtsurf = my_font.render('T _e_t _ _ _ \n blah, blah blah! \n',False,(0, 0, 0))

while 1:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT: sys.exit()

        screen.fill(white)
        screen.blit(stage,stagerect)
        screen.blit(txtsurf,(0,0))
        pygame.display.flip()
