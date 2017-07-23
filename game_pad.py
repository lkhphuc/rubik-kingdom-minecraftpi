import mcpi.minecraft as minecraft
import mcpi.block as block
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import random
mc = minecraft.Minecraft.create()

SIZE3 = 12;
SIZE2 = 9;
SIZE1 = 6;
color= [0,4,1,14,11,5,6,9,2]
#initial setup for keypad
MATRIX = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]
pin_in = [19,21,23,29]
pin_out = [31,33,35,37]
for i in range(4):
	GPIO.setup(pin_in[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
for j in range(4):
	GPIO.setup(pin_out[j], GPIO.OUT)
	GPIO.output(pin_out[j], 1)


def board(x,y,z,size):
	#borders
	mc.setBlocks(x,y,z,x+size,y,z+size,35,15);
	mc.setBlocks(x+1,y,z+size/3,x+1,y,z+size-size/3,102) #special block for x,z identification
	mc.postToChat("Please stand on the glass block to get the view of the puzzle.")
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
	
	mc.postToChat("When done, press any button to check if you win or press 1 anytime to quit.")
	for i in range(size-3):
		for j in range(size-3):
			a = mc.getBlockWithData(x+2+i,y,z+2+j)
			if a.data == 2:
				mc.setBlock(x+2+i,y,z+2+j,0)
				posi = [x+2+i,z+2+j]
				return posi
	
def model(x,y,z):		
	q = 0		
	for i in range(3):
		for j in range(3):
			mc.setBlock(x+i,y,z+j,35,color[q])
			q = q+1	

#pass in pos of smallest x and z in game,size of board and position of air block
def game(X,y,Z,SIZE,x,z):
	finish = False 
	X2= X +SIZE-4
	Z2= Z +SIZE-4
	while finish == False:
		move = keypad();
		if (move == "2") and (x > X):
			teleport(x,y,z,x-1,y,z)
			x = x-1
		elif (move == "6") and (z > Z):
			teleport(x,y,z,x,y,z-1)
			z=z-1
		elif (move == "4") and (z < Z2):
			teleport(x,y,z,x,y,z+1)
			z = z+1;
		elif (move == "8") and (x < X2):
			teleport(x,y,z,x+1,y,z)
			x = x+1
		elif (move == "1"):
			finish = True
			mc.postToChat("You quit the game. :(")
		else :	
			finish = condition(X,y,Z,SIZE)
			if finish == True:
				mc.postToChat("Congratulation. You win the game. :)")

def teleport(x,y,z,X,Y,Z):
	a = mc.getBlockWithData(X,Y,Z)
	mc.setBlock(x,y,z,a.id,a.data)
	mc.setBlock(X,Y,Z,0)

#pass in pos of smallest x, z and size of board
def condition(x,y,z,SIZE):
    finish = True #condition of all checked block
    for i in range(SIZE-3):
        if ( i < (SIZE-3)/3 and finish):
            for j in range(SIZE-3):
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 0:
                        finish = False
                elif ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 4:
                        finish = False
                elif finish:
                    if a.data != 1:
                        finish = False
        elif ( i < (SIZE-3)/3*2 and finish ):
            for j in range(SIZE-3):
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 14:
                        finish = False
                elif ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 11:
                        finish = False
                elif finish:
                    if a.data != 5:
                        finish = False          
        elif finish:
            for j in range(SIZE-3):
                a = mc.getBlockWithData(x+i,y,z+j)
                if ( j < (SIZE-3)/3 and finish):
                    if a.data != 6:
                        finish = False
                elif ( j < (SIZE-3)/3*2 and finish):
                    if a.data != 9:
                        finish = False                    
                elif (i == SIZE-4 and j == SIZE-4):
                   if a.id != 0:
                       finish = False
                elif a.data != 2:
                   finish = False    
    return finish

def keypad():
	waiting = True
	while (waiting):
		for i in range(4):
			GPIO.output(pin_out[i],0)
			for j in range(4):
				if GPIO.input(pin_in[j]) == 0:
					val = MATRIX[j][i]
					waiting = False
					while (GPIO.input(pin_in[j]) == 0):
						pass
			GPIO.output(pin_out[i],1)
	return val

pos = mc.player.getTilePos()
posi = board(pos.x,pos.y,pos.z,SIZE1)
model(pos.x,pos.y,pos.z+SIZE1+1)

game(pos.x+2,pos.y,pos.z+2,SIZE1,posi[0],posi[1]) 

#clean up before exit
GPIO.cleanup()