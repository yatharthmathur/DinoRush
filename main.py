from object import *

def main():
    #Initialising window.
    pygame.init()
    pygame.display.set_caption("DinoRush")
    screen = pygame.display.set_mode(DISPLAY, OPENGLBLIT|DOUBLEBUF|OPENGL)
    init()

    clock = pygame.time.Clock()
    print(loadTexture())
    #empty object list
    cacti = []
    birds = []
    player = Player()
    flag=0
    prev = []
    space = 0
    down = 0
    collision=0
    score = 0
    fps = 70
    lose = 0
    paused = 0
    background()
    pygame.display.flip()
    while True:



        while not paused:
            background()
            score += 0.1

            #to refresh each cycle frame
            draw_text(str(int(score)), DISPLAY[0] / 2, 550)
            if(score % 100 == 0):
                fps+=5
            clock.tick(fps)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == K_SPACE or event.key == K_w or event.key == K_UP):
                        if player.y <=35:
                            space = 1

                    if event.key == K_s or event.key == K_DOWN:
                        down = 1

                    if event.key == K_ESCAPE:
                        paused = 1
                        print("Your score is : ", int(score))
                        print("Press escape to exit or any other key to continue.")

                if event.type == pygame.KEYUP:
                    if event.key == K_s or event.key == K_DOWN:
                        down = 0

            if collision:
                paused = 1
                print("GAME OVER : Your score is : ", int(score))
                print("Press escape to exit or any other key to continue.")

            #if height is less than 200 the player moves up
            if(space):
                player.jump()
                if(player.y >=200):
                    space=0
            else:
                player.gravity()

            #jump cancelling and cannot duck while jumping or vice versa
            player.duck(down)
            if down:
                space=0



            #selector for bird or cactus randomization
            select = random.randint(0,2)

            #if the lists are empty then fill at least one
            if flag == 0:
                if(select):
                    cactus = Cacti()
                    cacti.append(cactus)
                    flag+=1
                    prev = cacti
                else:
                    bird = Bird()
                    birds.append(bird)
                    flag+=1
                    prev = birds


            if flag >= 1:
                #whichever was the list that was appended to last is used as a reference for the next obstacle
                if(prev[-1].x >=200 and prev[-1].x <=random.randint(200,505)):
                    if(select):
                        cactus = Cacti()
                        cacti.append(cactus)
                        flag+=1
                        prev = cacti

                    else:
                        bird = Bird()
                        birds.append(bird)
                        flag+=1
                        prev = birds

            #remove obstacle from memory if they exceed lower limit
            remove(cacti)
            remove(birds)

            #move each obstacle with speed specified
            movement(cacti,CACT_SPEED)
            movement(birds,BIRD_SPEED)

            #collision detection

            if(collisionBird(birds,player)):
                collision = 1
                gameOver(score)
            if(collisionCactus(cacti,player)):
                collision = 1
                gameOver(score)


            player.render()

            pygame.display.flip()



        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    if collision:
                        cacti = []
                        birds = []
                        player = Player()
                        flag=0
                        prev = []
                        space = 0
                        down = 0
                        collision=0

                        fps = 70
                        lose = 0
                        paused = 0


                        score = 0
                        draw_text(str(int(score)), DISPLAY[0] / 2, 550)

                        pygame.display.flip()
                    else:
                        paused = 0

#run main
main()
