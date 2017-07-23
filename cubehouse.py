import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

SIZE = 12

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
x2 = x + SIZE/4 + 1
y2 = y + SIZE/4 + 1
z2 = z + SIZE/4 + 1
x3 = x2 + SIZE/4 + 1
y3 = y2 + SIZE/4 + 1
z3 = z2 + SIZE/4 + 1
#outer block
mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,35,7)
#carved the inside
mc.setBlocks(x+1,y+1,z+1,x+SIZE-1,y+SIZE-1,z+SIZE-1,0)
#up white
for i in range(SIZE-1):
	if ( x+i+1 != x2 and x+i+1 != x3):
		for j in range(SIZE-1):
			if ( z+j+1 != z2 and z+j+1 != z3):
				mc.setBlock(x+i+1,y+SIZE,z+j+1,80)
#down yellow
for i in range(SIZE-1):
	if ( x+i+1 != x2 and x+i+1 != x3):
		for j in range(SIZE-1):
			if ( z+j+1 != z2 and z+j+1 != z3):
				mc.setBlock(x+i+1,y,z+j+1,41)
#side 1 green
for i in range(SIZE-1):
	if ( z+i+1 != z2 and z+i+1 != z3):
		for j in range(SIZE-1):
			if ( y+j+1 != y2 and y+j+1 != y3):
				mc.setBlock(x,y+j+1,z+i+1,35,5)	
#side 2 blue
for i in range(SIZE-1):
	if ( z+i+1 != z2 and z+i+1 != z3):
		for j in range(SIZE-1):
			if ( y+j+1 != y2 and y+j+1 != y3):
				mc.setBlock(x+SIZE,y+j+1,z+i+1,22)	
#side 3 red
for i in range(SIZE-1):
	if ( x+i+1 != x2 and x+i+1 != x3):
		for j in range(SIZE-1):
			if ( y+j+1 != y2 and y+j+1 != y3):
				mc.setBlock(x+i+1,y+j+1,z,35,1)	
#side 4 orange
for i in range(SIZE-1):
	if ( x+i+1 != x2 and x+i+1 != x3):
		for j in range(SIZE-1):
			if ( y+j+1 != y2 and y+j+1 != y3):
				mc.setBlock(x+i+1,y+j+1,z+SIZE,35,14)	
