import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

SIZE3 = 12;
SIZE2 = 9;
SIZE1 = 6;
color= [0,4,1,14,11,5,6,9,2]

def board(x,y,z,size):
	#borders
	mc.setBlocks(x,y,z,x+size,y,z+size,35,15);
	mc.setBlocks(x+2,y,z+2, x+size-2,y,z+size-2,0)
	mc.setBlock(x+1,y,z+2,0)
	mc.setBlocks(x-1,y,z+size/3,x-1,y,z+size-size/3,35,15) #special block for x,z identification
	#random block
	Matrix = [[0 for i in range(size-3)] for i in range(size-3)]
	for i in range(9):
		for j in range(((size-3)/3)*((size-3)/3)):
			while True:
				ranx = random.randint(0,size-4)
				ranz = random.randint(0,size-4)
				if Matrix[ranx][ranz] == 0 :
					mc.setBlock(x+2+ranx,y,z+2+ranz,35,color[i])
					Matrix[ranx][ranz] = 1;
					break;

#pass in pos of empty block and size of board
def game(x,y,z,SIZE): 
	while !condition(x,y,z,SIZE):
		move = raw_input("Enter your move: ");
		if (move == "8") and (x < SIZE-3 and z < SIZE-3):
			teleport(x,y,z,x-1,y,z)
			x = x-1
		elif (move == "6") and (x < SIZE-3 and z < SIZE-3):
			teleport(x,y,z,x,y,z-1)
			z=z-1
		elif (move == "4") and (x < SIZE-3 and z < SIZE-3):
			teleport(x,y,z,x,y,z+1)
			z = z+1;
		elif (move == "2") and (x < SIZE-3 and z < SIZE-3):
			teleport(x,y,z,x+1,y,z)
			x = x+1

def teleport(x,y,z,X,Y,Z):
	a = mc.getBlockWithData(X,Y,Z)
	mc.setBlock(x,y,z,a.id,a.data)
	mc.setBlock(X,Y,Z,0)

#pass in pos of empty block and size of board
def condition(x,y,z,SIZE):
    x = x+1;
    finish = True #condition of finish all checked block
    a = mc.getBlockWithData(x+i+1,y,z+j) 
    for i in range(SIZE-3):
        if ( i < (SIZE-3)/3 and finish):
            for j in range(SIZE-3):
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 0:
                        finish = False;
                else if ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 4:
                        finish = False;
                else if finish:
                    if a.data != 1:
                        finish = False;
        else if ( i < (SIZE-3)/3*2 and finish ):
            for j in range(SIZE-3)
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 14:
                        finish = False;
                else if ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 11:
                        finish = False;
                else if finish:
                    if a.data != 5:
                        finish = False;            
        else if finish:
            for j in range(SIZE-3)
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 6:
                        finish = False;
                else if ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 9:
                        finish = False;
                else if finish:
                    if a.data != 2:
                        finish = False;    
    return finish

pos = mc.player.getTilePos()
board(pos.x,pos.y,pos.z,SIZE2)
game(pos.x+1,pos.y,pos.z+2,SIZE2) 
