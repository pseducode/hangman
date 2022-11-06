import sys,pygame
pygame.init()
size = width, height = 1000, 600
black= 0, 0,0
white=255, 255,255


screen = pygame.display.set_mode(size)

stage = pygame.image.load("stage.png")
stagerect = stage.get_rect()
my_font = pygame.font.SysFont('Comic Sans MS',30)
base_font = pygame.font.Font(None, 32)
txtsurf = my_font.render('T _e_t _ _ _ \n blah, blah blah! \n',False,(0, 0, 0))

clock = pygame.time.Clock()
usertxt=''
inprect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False
while 1:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inprect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_BACKSPACE:
                usertxt = usertxt[:-1]
            else:
                usertxt +=event.unicode

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, inprect)
        inrectsurf = base_font.render(usertxt, True, (255, 255, 255))
        #screen.fill(white)
        screen.fill(black)
        screen.blit(stage,(width-983,height-436))
        screen.blit(txtsurf,(width-txtsurf.get_width(),height-txtsurf.get_height()))
        screen.blit(inrectsurf, (0,0))
        inprect.w = max(100, inrectsurf.get_width()+10)
        pygame.display.flip()
        clock.tick(60)
 
