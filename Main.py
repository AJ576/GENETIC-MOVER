from mover import mover
import pygame
import sys
import random
import math

#Intital variables
gen = 1
bestMove = [[],10000]
bois = [] #bois is a list of the movers
moves = 150 # a limitied number of moves is given to each mover in a generation. This is to make sure we can get to the next gen
goal = [750,300]
mutation_rate = 0.10
reached = False

#initializing the pygame screen and other important things

pygame.init()

DISPLAY=pygame.display.set_mode((800,600),0,32)
BLACK=(2,2,2)
BLUE=(0,0,150)
RED=(200,0,0)

DISPLAY.fill(BLACK)
clock = pygame.time.Clock()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 20)
text_surface = my_font.render('Generation:', False, (255, 255, 255))


#Generates a set of directions( or a map) for the mover to follow
def generate_moves():
    first_moves = []
    i = 0
    
    while(i<moves):
        first_moves.append(random.randint(0,2)) 
        i+=1
    return first_moves

#mutates the move according to the mutation rate. This allows the next gen to take the fittest moveset from previous generation and evolve from it.
def mutate(move):
        i = 0
        moves = []
        while(i<len(move)):
            r = random.random()
            # print(len(self.moves))
            # print(i)
            if(r<mutation_rate):

                #if going forward
                if(move[i]==0):
                    rand=random.random()
                    if(rand<0.5):
                        moves.append(1)
                    else:
                        moves.append(2)
                    
                
                #if going up
                
                elif(move[i]==1):
                    rand=random.random()
                    if(rand<0.5):
                        moves.append(0)
                    else:
                        moves.append(2)


                #if going down

                elif(move[i]==2):
                    rand=random.random()
                    if(rand<0.5):
                        moves.append(0)
                    else:
                        moves.append(1)
            else:
                num = move[i]
                moves.append(num)
            i+=1

        return moves

#Sets the inital generation
def init_gen():
    
        bois.clear()
        i = 0
        #let's make 100 bois
        num = 100

        #initializes each mover/boi
        while(i<num):

            moves = generate_moves()
            bois.append(mover([50,0],moves))
            i+=1
        

#Sets every generation after the initial generation by mutating the best moveset from the previous generation     
def next_gen():
        i = 0
        num = len(bois)
        bois.clear()
        while(i<num):
            
            #instead of generating moves, we are mutating from a previous moveset
            moves11 = mutate(bestMove[0])
            bois.append(mover([50,0],moves11))  
            i+=1
        


#iterates over each movers moveset and depending on which mover reached closest to the goal, updates the list of the best moveset of this generation
def bestFit():
    i = 0
    num = len(bois)
    while(i<num):
        bMove = bois[i].getFitness()
        if(bestMove[1]>bMove[1]):
            bestMove[0]=bMove[0]
            bestMove[1]=bMove[1]
        i+=1

#finds the distance to the gaol using the distance formula
def findDistance(i,goalPos):

    pos = bois[i].getPos()
    diss = math.dist(pos,goalPos)
    bois[i].setDistance(diss)


#draws each generation on the screen.
def move(j):
    global reached
    i = 0
    num = len(bois)
    
    while(i<num):
        bois[i].move(j)
        findDistance(i,goal)
        pos = bois[i].getPos()

        #an if statement to check if the bois have reached.
        if(bois[i].getReached()):
            reached = True

        #display them when they move
        pygame.draw.rect(DISPLAY,BLUE,(pos[0],pos[1],10,10))
        pygame.display.flip()
        i+=1
        
    
def simulation(gen):
    global reached
    while(not reached):
    
            g = str(gen)
            numm = my_font.render(g, False, (255, 255, 255))


            #depending on the generation, we either initialize the first generation or mutate and initialize the next generation
            k = 0
            if(gen < 2):
                init_gen()
            else:
                next_gen()
    
            while(k<moves):
                move(k)
                k+=1
                
                DISPLAY.fill(BLACK)
                pygame.draw.rect(DISPLAY,RED,(goal[0],goal[1],30,30))
                DISPLAY.blit(text_surface, (500,5))
                DISPLAY.blit(numm, (615,5))
                clock.tick(10)
            
            bestFit() 
            gen+=1

        #showing the conclusion
            if (reached):
                DISPLAY.blit(my_font.render("Goal Was Reached after {} generations".format(gen), False, (255, 255, 255)), (150,200))
                pygame.display.flip()
        

def main(gen):
    
    running = True
    while (running == True): #will keep going until we find a very close goal reaching move set

        simulation(gen)

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                running=False
                

    pygame.quit()
    sys.exit()

main(gen)


