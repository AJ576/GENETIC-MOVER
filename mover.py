
#This is the classs that provides property for a mover or the square that will move towards the goal
class mover:

    #each mover has it's intital position, and moves(which gives the direction) on each turn provided by the enviorment
    #The speed and distace is given by us.
    #The distance gives the distace from the goal. It's set at a high value from the begining and updates as the mover moves either towards, or away from the goal
    def __init__(self,pos,moves):
        self.pos=pos
        self.distance=10000
        self.moves=moves
        self.reached = False
        self.speed = 10

    #For debugging
    def prMoves(self):
        print(self.moves)

    #Each mover has a fitness level and depending on the fitness, the simulation decides if the movers traits will be passed on to the next gen
    def getFitness(self):
        return [self.moves,self.distance]
    
    #gets position
    def getPos(self):
        return self.pos

        #returns the reached variable's value
    def getReached(self):
        self.goal()
        return self.reached

    #sets the distance
    def setDistance(self,dis):
        self.distance = dis
    
    def move(self,i):
        
        if(self.moves[i]==0):
            self.pos[0]+=self.speed
        if(self.moves[i]==1):
            self.pos[1]+=self.speed
        if(self.moves[i]==2):
            self.pos[0]-=self.speed
    
    #Updates the cell's reached status to become true when goal is reached
    def goal(self):
        if(self.distance<25):
            self.reached = True
            self.speed = 0
            


print("TEST COMPLETE")

    
        