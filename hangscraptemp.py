
def betterspacegame():# game loop with fixed indentation, from playgame4
    #first initstuff
    pygame.init()
    size = width, height = 1000, 600
    black = 0, 0,0
    white = 255, 255,255
    screen = pygame.display.set_mode(size)
    loadsdtages() # load in stage graphics to global vat
    varsletterin="" #input placeholder
    modepicked = False #value to determine if picked difficulty/a solution yet
    clock = pygame.time.Clock()
    while True: ## main game loop
        if not modepicked: #Haven't picked difficulty yet, prompt for input
            msg = texttosurf("Please enter difficulty desired (easy, medium, or hard: )"+letterin)
        #deal with input
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
            elif event.type == pygame.KEYDOWN: #pressed a key, deal with items
                if event.key == pygame.K_BACKSPACE: #hit delete/ so delete currenbt char
                    letterin = letterin[:-1]
                elif ((event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN)): #hit enter so validate input, etc
                    if not modepicked: # haven't picked a difficulty previous so validate setting + start game
                        if letterin in options: #yay, entered valid difficulty, so setup game
                             modepicked= True
                             msg = texttosurf("Okay, now picking a solution of difficulty: "+letterin) #Tell user picked valid difficulty
                             solution = picksolution(letterin) #actually pick solution with desired difficulty
                             b=board2.board2(solution)# init board
                             letterin="" #reset inouyt string
                        else: #picked bad gamemode, ask for reset
                            msg = texttosurf("Sorry, "+letterin+"is nbot a valid difficulty sdetting plerase re-enter a valid one!")
                            letterin=""
                    else: #already picked a game mode, so update board with guess
                        state = b.makeguess(letterin)
                        msg = texttosurf(b.boardstatus())
                        
                else: #pressed a non-special key, add to input
                    letterin+=event.unicode
                    
        #write shit to screen
        stageimage = stageimages[b.howmanywrong()]
        