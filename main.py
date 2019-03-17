from object import *

def main():
    #Initialising window.
    pygame.init()
    pygame.display.set_caption("SuperDinoBros")
    screen = pygame.display.set_mode(DISPLAY, OPENGLBLIT|DOUBLEBUF|OPENGL)
    init()
    pygame.font.init()

    clock = pygame.time.Clock()

    #Setting perspective
    glClear(GL_COLOR_BUFFER_BIT);

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

    while True:

        score += 1
        #to refresh each cycle frame
        glClear(GL_COLOR_BUFFER_BIT)
        clock.tick(70)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and player.y<=60:
                    space = 1
            if event.type == pygame.KEYDOWN:
                if event.key == K_s or event.key == K_DOWN:
                    down = 1
            if event.type == pygame.KEYUP:
                if event.key == K_s or event.key == K_DOWN:
                    down = 0

        if collision :
            print("GAME OVER: Your score was : " + str(int(score)))
            pygame.quit()
            quit()




        if(space):
            player.jump()
            if(player.y >=200):
                space=0

        else:
            player.gravity()

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

        if(collisionCactus(cacti,player)):
            collision = 1



        player.render()


        #draw everything
        glFlush()
        pygame.display.flip()




#run main
main()
