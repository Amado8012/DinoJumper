import pygame 
import random 

#print("hellow world")#left for testing purposes
pygame.init()
screen = pygame.display.set_mode((649,480))
pygame.display.set_caption("Dino Jumper")
doExit=False
clock = pygame.time.Clock()
#game variables go here, above the game loop
p1x = 20
p1y = 200
xVel = 0
yVel = 0

#create and initalize a 5-slot list
CactusHeights= [80,40,20,80,30]

CactusXpos=[] #creates an empty list

for x in range(5): #a for loop that runs 5 times 
    #the append function adds an entry to our array
    CactusXpos.append(random.randrange(200,3000))

#game loop##############
while not doExit:
    #timer aka input section///////////////
    clock.tick(60)
    for event in pygame.event.get(): #Event Queue!
        if event.type == pygame.QUIT:
            doExit = True

    #check for player/cactus collision 
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-y), (30, 80))
        b = pygame.Rect((p1x, p1y), (20, 20))
        if a.colliderect(b) == True: 
            print("COLLITION")
            doExit=True
            #winsound.Beep(900.900)

    #update cactus location if they're off the screen 
    for x in range(len(CactusXpos)): 
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640, 5000)
            # print("reset to ", CactusXpos[x]) #used for testing

    #move cactus
    CactusXpos = [x - 5 for x in CactusXpos]

    CactusImg = pygame.image.load('cactus.png')

    #put keyboard input here

   #update position by adding velocity to position 
    p1y += yVel 

    #turn off flying 
    if (p1y+30) >= 480:
        TouchGround = True
    else:
        TouchGround = False 

    CactusImg = pygame.image.load('cactus.png')

    #PHYSICS---------------------------------------
    #gravit! this goe sin your timer section 
    if TouchGround == False:
        yVel+=.5#make this bigger to increase gravity
    else:
        yVel = 0

    
     #input section//////////////
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and TouchGround == True:
        yVel=-10#make this bigger to jump higher
    




    #render section//////////////
    screen.fill((0,0,0))

    #draw cactuses
    for x, y in zip(CactusXpos, CactusHeights):
        screen.blit(CactusImg, (x-15,480-y))


    #put draw rectangle here 
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 20), 1)

    pygame.display.flip()
#end game loop###############

pygame.quit()
