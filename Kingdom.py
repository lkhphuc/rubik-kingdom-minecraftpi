from mcpi import minecraft
from time import sleep
import random

mc = minecraft.Minecraft.create()
air = 0
dirt = 3
grass = 2
wool = 35
glass = 95

mc.postToChat("Welcome to the Rubik Kingdom!")

#Clear land
mc.setBlocks(-128,1,-128,128,128,128,air)
mc.setBlocks(-128,-1,-128,128,-128,128,dirt)
mc.setBlocks(-128,0,-128,128,0,128,grass)


##############################################################
#                        Functions                           #
##############################################################

#Battlements Function to build battlements at the top of gate, wall and castle
def Battlements(x, y, z, side,color):
        for i in range(3):
                for j in range(side):
                        mc.setBlock(x+j,y+i,z,wool,color)
                        if (i!=0)and ((j%4==2)or(j%4==3)):
                                mc.setBlock(x+j,y+i,z,air)

        for i in range(3):
                for j in range(side):
                        mc.setBlock(x,y+i,z+j,wool,color)
                        if (i!=0)and ((j%4==2)or(j%4==3)):
                                mc.setBlock(x,y+i,z+j,air)
        for i in range(3):
                for j in range(side):
                        mc.setBlock(x+side-1,y+i,z+j,wool,color)
                        if (i!=0)and ((j%4==2)or(j%4==3)):
                                mc.setBlock(x+side-1,y+i,z+j,air)
        for i in range(3):
                for j in range(side):
                        mc.setBlock(x+j,y+i,z+side-1,wool,color)
                        if (i!=0)and ((j%4==2)or(j%4==3)):
                                mc.setBlock(x+j,y+i,z+side-1,air)

#Wall function to build four wall covering the world
def Wall(x,y,z):
        mc.setBlocks(x,y,z,x+230,y+16,z+230,wool,15)
        mc.setBlocks(x+4,y,z+4,x+226,y+16,z+226,air)

	color = [0,1,2,3,4,5,6,9,10,11,13,14]	

        for i in range(57):
                for j in range(4):
                        mc.setBlocks(x+1+4*i,y+1+4*j,z,x-1+4*(i+1),y-1+4*(j+1),z+3,wool,color[random.randint(0,11)])
        for i in range(57):
                for j in range(4):
                        mc.setBlocks(x+1+4*i,y+1+4*j,z+227,x-1+4*(i+1),y-1+4*(j+1),z+229,wool,color[random.randint(0,11)])

#House function to build houses in village						
def House(x, y, z, side, material1, border, material2, fcolor, lcolor, bcolor, rcolor, ucolor):
        s = (side-4)/3 + 1

        # front wall
        mc.setBlocks(x,y,z,x-1+side,y-1+side,z,material1,border)
        # Create color blocks
        for i in range(3):
                for j in range(3):
                        mc.setBlocks(x + 1 + i*s,y + 1 + j*s,z,x-1+(i+1)*s,y-1+(j+1)*s,z,material2,fcolor)

        # left wall
        mc.setBlocks(x-1+side,y,z,x-1+side,y-1+side,z-1+side,material1,border)
        for i in range(3):
                for j in range(3):
                        mc.setBlocks(x-1+side,y+1+i*s,z+1+j*s,x-1+side,y-1+(i+1)*s,z-1+(j+1)*s,material2,lcolor)

        # back wall
        mc.setBlocks(x-1+side,y,z-1+side,x,y-1+side,z-1+side,material1,border)
        for i in range(3):
                for j in range(3):
                        mc.setBlocks(x-1+(i+1)*s,y+1+j*s,z-1+side,x+1+i*s,y-1+(j+1)*s,z-1+side,material2,bcolor)

        # right wall
        mc.setBlocks(x,y,z-1+side,x,y-1+side,z,material1,border)
        for i in range(3):
                for j in range(3):
                        mc.setBlocks(x,y+1+j*s,z-1+(i+1)*s,x,y-1+(j+1)*s,z+1+i*s,material2,rcolor)

        # up wall
        mc.setBlocks(x,y-1+side,z,x-1+side,y-1+side,z-1+side,material1,border)
        for i in range(3):
                for j in range(3):
                        mc.setBlocks(x+1+i*s,y-1+side,z+1+j*s,x-1+(i+1)*s,y-1+side,z-1+(j+1)*s,material2,ucolor)

#Create a front door for a house						
def OneDoor(x, y, z, side):
	s = (side-4)/3 + 1
	mc.setBlocks(x+1+s,y,z,x-1+2*s,y-1+2*s,z,air)

#Create four doors for special ones
def FourDoor(x, y, z, side):
        s = (side-4)/3 + 1
        mc.setBlocks(x+1+s,y,z,x-1+2*s,y-1+2*s,z,air)
        mc.setBlocks(x,y,z+1+s,x,y-1+2*s,z-1+2*s,air)
        mc.setBlocks(x+1+s,y,z-1+side,x-1+2*s,y-1+2*s,z-1+side,air)
        mc.setBlocks(x-1+side,y,z+1+s,x-1+side,y-1+2*s,z-1+2*s,air)

#Create windows
def Window(x, y, z, side):
        s = (side-4)/3 + 1
        mc.setBlocks(x+1+s,y+1+s,z,x-1+2*s,y-1+2*s,z,air)
        mc.setBlocks(x,y+1+s,z+1+s,x,y-1+2*s,z-1+2*s,air)
        mc.setBlocks(x+1+s,y+1+s,z-1+side,x-1+2*s,y-1+2*s,z-1+side,air)
        mc.setBlocks(x-1+side,y+1+s,z+1+s,x-1+side,y-1+2*s,z-1+2*s,air)

#Build fortress next to the main castle
def Fortress(x,y,z,side):
	for i in range(3):
		House(x,y+i*(side-4),z,side,wool,0,wool,5,1,3,14,4)
		Window(x,y+i*(side-4),z,side)
		House(x-1+3*(side-1),y+i*(side-4),z,side,wool,0,wool,5,14,3,1,4)
		Window(x-1+3*(side-1),y+i*(side-4),z,side)

	Battlements(x,y+3*(side-3),z,side,0)
	Battlements(x-1+3*(side-1),y+3*(side-3),z,side,0)

#Build the temple's base
def TempleBase(x, y, z, side, stair, material):
        s = side/2
        w = (side-stair)/2

        for i in range(s-9):
                mc.setBlocks(x+i,y+i,z+i,x-1+side-i,y+i,z-1+side-i,material,0)
        mc.setBlocks(x,y,z,x+w,y+s,z+w,air)
        mc.setBlocks(x+w+stair,y,z,x+2*w+stair,y+s,z+w,air)
        mc.setBlocks(x,y,z+w+stair,x+w,y+s,z+2*w+stair,air)
        mc.setBlocks(x+w+stair,y,z+w+stair,x+2*w+stair,y+s,z+2*w+stair,air)

        for i in range(s-8):
                mc.setBlocks(x+w+2,y+i,z+i,x-2+w+stair,y+1+i,z+1+i,air)
        for i in range(s-8):
                mc.setBlocks(x+w+2,y+i,z+side-i,x-2+w+stair,y+1+i,z-1+side-i,air)
        for i in range(s-8):
                mc.setBlocks(x+i,y+i,z+w+2,x+1+i,y+1+i,z-2+w+stair,air)
        for i in range(s-8):
                mc.setBlocks(x+side-i,y+i,z+w+2,x-1+side-i,y+1+i,z-2+w+stair,air)

#Build the temple's inside base
def TempleInside(x, y, z, side, material):
        s = side/2
        color = [14,5,1,3]
        for i in range(s-10):
		mc.setBlocks(x+2*i,y+4*i,z+2*i,x-1+side-2*i,y+3+4*i,z-1+side-2*i,material,color[i])

#Build the welcome gate
def Gate(x,y,z,side):
        s = (side-4)/3 + 1
        for i in range(3):
                House(x,y+i*(side-1),z,side,wool,0,wool,1,3,14,5,4)
                Window(x,y+i*(side-1),z,side)
                House(x+2+3*(side-1),y+i*(side-1),z,side,wool,0,wool,1,3,14,5,4)
                Window(x+2+3*(side-1),y+i*(side-1),z,side)

        Battlements(x,1+y+3*(side-1),z,side,0)
        Battlements(x+2+3*(side-1),1+y+3*(side-1),z,side,0)

        for i in range(2):
                for j in range(2):
                        House(x+1+(i+1)*(side-1),y+j*(side-1),z,side,wool,0,wool,1,3,14,5,4)

        mc.setBlocks(x+2+side,y,z+1,x+3*side,y-2+2*side,z+side-2,wool)
        mc.setBlocks(x+1+side+s,y,z,x+2+side+4*s,y+2+4*s,z+side,air)

        for i in range(3):
                for j in range(2*side-1):
                        mc.setBlock(x+side+j,y-1+2*side+i,z,wool,0)
                        if (i!=0)and ((j%4==1)or(j%4==2)):
                                mc.setBlock(x+side+j,y-1+2*side+i,z,air)
        for i in range(3):
                for j in range(2*side-1):
                        mc.setBlock(x+side+j,y-1+2*side+i,z-1+side,wool,0)
                        if (i!=0)and ((j%4==1)or(j%4==2)):
                                mc.setBlock(x+side+j,y-1+2*side+i,z-1+side,air)

#Build a river in the middle of the world
def River(z,width):
	mc.setBlocks(-128,-8,z-5,128,0,z+width+5,45)
	mc.setBlocks(-128,-7,z,128,0,z+width,air)
	mc.setBlocks(-128,-7,z,128,-2,z+width,8)

#Build roads across the world
def Roadx(x):
	mc.setBlocks(x,0,-128,x+17,0,128,45)
	mc.setBlocks(x+2,0,-128,x+15,0,128,24)
	
def Roadz(z):
	mc.setBlocks(-128,0,z,128,0,z+8,45)
	mc.setBlocks(-128,0,z+1,128,0,z+7,24)

#Create Trees
def Tree(x,y,z):
	for i in range(0,15):
		mc.setBlock(x, y+i, z, 17)
	y=y+10
	for a in range (0,4):
		if(a==0):
			for i in range(0,6):
				mc.setBlock(x, y, z+i, 17)
			z=z+5
			for i in range(0,4):
				mc.setBlock(x+i, y, z, 17)
				mc.setBlock(x-i, y, z, 17)
			x=x+3
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y ,z+i, 35, r)
				y=y+1
			x=x-7
			y=y-6
			x = x+1
			z = z+1
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y=y+1		
		elif(a==1):
			x=x+5
			z=z-4
			y=y-6
			for i in range(0,6):
				mc.setBlock(x+i, y, z, 17, 1)
			x=x+5
			for i in range(0,4):
				mc.setBlock(x, y, z+i, 17, 1)
				mc.setBlock(x, y, z-i, 17, 1)
			z = z-3
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			y = y+3
			x = x-1
			z = z-1
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y = y+1
			z = z+6
			x = x+1
			z = z+1
			y = y-6
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y = y+1
		elif(a==2):
			y=y-6
			z=z-1
			x=x-4
			for i in range(0,6):
				mc.setBlock(x, y, z-i, 17, 1)
			z = z-6
			for i in range(0,4):
				mc.setBlock(x+i, y, z, 17, 1)
				mc.setBlock(x-i, y, z, 17, 1)
			x = x-3
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y=y+1
			y=y-6
			z=z+1
			x=x+7
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y = y+1
		else:
			y=y-6
			x = x-1
			z = z+6
			for i in range(0,6):
				mc.setBlock(x-i, y, z, 17, 1)
			x = x-6
			for i in range(0,4):
				mc.setBlock(x, y, z-i, 17, 1)
				mc.setBlock(x, y, z+i, 17, 1)
			z = z+3
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y=y+1
			z = z-6
			y = y-6
			x = x+1
			z = z+1
			for i in range(0,4):
				mc.setBlock(x, y+i, z, 17, 1)
			x = x-1
			z = z-1
			y = y+3
			for n in range(0,3):
				for i in range(0,3):
					for j in range(0,3):
						r = random.randint(0,15)
						mc.setBlock(x+j, y, z+i, 35, r)
				y=y+1
	z = z+3
	y = y-3
	x = x+4
	for n in range(0,3):
		for i in range(0,3):
			for j in range(0,3):
				r = random.randint(0,15)
				mc.setBlock(x+j, y, z+i, 35, r)
		y = y+1			

#Create Bridge
def Bridge(x,y,z):
	for j in range(0,3):
		for i in range(0,9):
			for a in range(0,11):
				for b in range(0,3):
					if(a>0 and a<9):
						mc.setBlock(x+1, y, z+b, 0)
					else:
						for m in range(0,4):
							for n in range(0,4):
								mc.setBlock(x+n, y,z+m, 17, 5)
						r = random.randint(0,15)
						for m in range(0,2):
							for n in range(0,2):
								mc.setBlock(x+m+1,y,z+n+1,35,r)
			z = z + 3
		z=z-27
		x=x+3
	y=y+1
	x=x-9
	mc.setBlocks(x, y, z, x+9, y, z+27, 17, 5)
	mc.setBlocks(x+1, y, z, x+9-1, y, z+27, 0)
	y=y+1
	mc.setBlocks(x, y, z, x+9, y ,z+27, 114)
	mc.setBlocks(x+1,y,z, x+9-1, y, z+27, 0)

	

#Create Garden
def Garden(x, y, z, width, height, length, color):
	mc.setBlocks(x,y,z,x+width,y+height,z+length,wool,color)
	mc.setBlocks(x+1,y,z+1,x-1+width,y+height,z-1+length,air)
	mc.setBlocks(x+1,y+1,z,x-1+width,y-1+height,z+length,air)
	
	
	SmallRubik()
##############################################################
#                            Main                            #
##############################################################

#Wall
Wall(-115,1,-102)
Battlements(-115,17,-102,231,15)
Battlements(-112,17,-99,225,15)
mc.setBlocks(-19,1,-107,19,30,-97,air)

#Gate
Gate(-19,1,-107,10)

#Road
Roadz(-97)
Roadz(-72)
Roadz(-47)
Roadx(-8)

#Village
def Village(x,z):
	House(x,1,z,10,wool,0,wool,11,1,5,14,4)
	OneDoor(x,1,z,10)
	House(x-15,1,z-3,13,wool,15,wool,5,1,11,14,4)
	OneDoor(x-15,1,z-3,13)
	House(x-27,1,z-3,10,wool,0,wool,1,5,14,11,4)
	OneDoor(x-27,1,z-3,10)
	House(x-45,1,z-4,16,wool,7,wool,4,1,11,14,5)
	OneDoor(x-45,1,z-4,16)

Village(-22, -85)
Village(-22, -60)
Village(-22, -35)

Village(60, -85)
Village(60, -60)
Village(60, -35)

#River
River(-20,20)

#Temple
TempleBase(-24,1,20,50,9,wool)
TempleInside(-13,1,31,28,wool)
House(-7,17,37,16,41,0,wool,1,3,14,5,4)
FourDoor(-7,17,37,16)

#Castle
Fortress(-23,1,74,13)
House(-10,1,70,22,wool,0,wool,1,11,14,5,0)
FourDoor(-10,1,70,22)
FourDoor(-32,1,70,22)
FourDoor(12,1,70,22)
House(-7,23,73,16,wool,0,wool,14,5,1,11,0)
Window(-7,23,73,16)
House(-4,39,77,10,wool,0,wool,11,1,5,14,4)
Window(-4,39,77,10)
Battlements(-10,23,70,22,0)
Battlements(-7,39,73,16,0)
Battlements(-4,49,77,10,0)

#Trees
for i in range(5):
	Tree(-10,1,-89+16*i)
for i in range(5):
	Tree(11,1,-89+16*i)

#Bridge
Bridge(-4,1,-24)

#Set player's position
mc.player.setPos(1,1,-120)
