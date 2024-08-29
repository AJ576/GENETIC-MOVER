#GENETIC MOVER AI 

Creator -  **ADITYA JHA**

This program simulates intelligence in a group of movers/cells by using the **genetic algorithm**

Time spent - 1 week

##DESCRIPTION - 
This program simulates a bunch of movers to reach a final destination. In each generation we have 100 movers. Each has an internal property called moves,which is like a map.It follows the moves to move on the screen. 
In the first generation, every mover recieves a random set of moves. Then the best performing mover in the first generation, calculated by how close it got to the goal in a finite amount of moves(150 in this case),
has their set of moves saved. The next generation is then fed in the best moveset of the previous generation but with slight mutations(i.e. changing the moveset at random places). The mutation rate is arbitararily 
set to be 10%. After making 150 moves again, the second generation's best moveset is taken and fed into the next generation, with mutations. This process takes place in every generation.
Gradually we can observe the movers getting closer to their goal as the generations come and go.

The program terminates when a generation arrives that includes cell that are able to reach the goal, in our case this is set to be 25 units geometric distace from the goal point.

The number of moves being limited to 150 is because each mover moves 10 units in any direction at each move, and the geometric distace from the start to the goal was calculated to be near the value of 1500 units. 
This value can be increased OR decreased, to affect the accuracy of path that the movers take. Beware, setting the number of moves too low will result in an infinte simulation as the movers will never be able to reach 
the goal in the limited moves.

The genetic mutation rate was set arbitararily and changing it can increase or decrease the number of generations required to reach the goal.

At the current values it takes around 18 genertions to reach the goal.

##ISSUES - 
If the user tries to close the program while the simulation is still running, it leads to the program crashing. 
Probable cause - Too many computations within one loop of the game.

##VIDEO WALKTHROUGH

Here's a walkthrough of my implemented program:

<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWZkNHR4OW05dWtvdHhxZmFvNjV6M3NlczMxejZ3emZyeHZkemNvOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pnh0ZJsgpkWUpYGfHx/giphy.gif' />

GIF created with [ScreenToGif](https://www.screentogif.com/) for Windows
