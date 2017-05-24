#!/bin/usr/python
import time
import os
import matrix
import person
from person import *
board=matrix.Matrix()

def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch


class Player(Person):
    def __init__(self,x,y):
		Person.__init__(self)
		self.x=x
		self.y=y
		self.adv_char=' '
		self.prev_char=' '
		self.onstair=0
		self.jump_dir='w'
		self.stage=0
		self.collided=0

    def move(self,ch,board,mario):
        if self.collided==1 and self.x==28 and self.y==1:
            self.prev_char=' '
        if self.prev_char=='O' or self.prev_char=='P':
            self.prev_char=' '
        if self.prev_char=='H':
            self.onstair=1
        else:
            self.onstair=0
        #Moving Up
        if (ch=='w' or ch=='W'):
            if(board.grid[self.x-1][self.y]=='H'):#If first block moving up is a staircase
                if(board.grid[self.x-2][self.y]=='H'):#Check its not BROKEN
                    self.adv_char=board.grid[self.x-1][self.y]
                    if self.adv_char=='P':
                    	if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                            self.adv_char='H'
                        else:
                            self.adv_char=' '
                    board.print_player(self.x,self.y,self.prev_char,mario)
                    self.x-=1
                    board.print_player(self.x,self.y,'P',mario)
                    self.prev_char=self.adv_char
                elif((board.grid[self.x-2][self.y]==' ') and (board.grid[self.x-1][self.y+1]=='X')):#If on second last step of a STAIRCASE
                    self.adv_char=board.grid[self.x-1][self.y]
                    if self.adv_char=='P':
                    	if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                            self.adv_char='H'
                        else:
                            self.adv_char=' '
                    board.print_player(self.x,self.y,self.prev_char,mario)
                    self.x-=1
                    board.print_player(self.x,self.y,'P',mario)
                    self.prev_char=self.adv_char
            elif((board.grid[self.x-1][self.y]==' ') and (board.grid[self.x][self.y+1]=='X')): #At The top of the stairs
                self.adv_char=board.grid[self.x-1][self.y]
                if self.adv_char=='P':
                    if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                        self.adv_char='H'
                    else:
                        self.adv_char=' '
                board.print_player(self.x,self.y,self.prev_char,mario)
                self.x-=1
                board.print_player(self.x,self.y,'P',mario)
                self.prev_char=self.adv_char
            if self.prev_char=='O':
                self.prev_char=' '
        #MovingDown
        if(ch=='s' or ch=='S'):
            if(board.grid[self.x+1][self.y]=='H'):#Moving down along stairs
                if((self.x+2<=29) and ((board.grid[self.x+2][self.y]=='H') ) ):
					#CHECK that its NOT BROKEN
                    if( self.x+2 == 29 ):
                        self.adv_char=board.grid[self.x+1][self.y]
                        if self.adv_char=='P':
                            if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                                self.adv_char='H'
                            else:
                                self.adv_char=' '
                        board.print_player(self.x,self.y,self.prev_char,mario)
                        self.x+=1
                        board.print_player(self.x,self.y,'P',mario)
                        self.prev_char=self.adv_char
                    elif((self.x+3<=29) and ((board.grid[self.x+3][self.y]=='H') or (board.grid[self.x+3][self.y]=='X')) ):
                        self.adv_char=board.grid[self.x+1][self.y]
                        if self.adv_char=='P':
                            if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                                self.adv_char='H'
                            else:
                                self.adv_char=' '
                        board.print_player(self.x,self.y,self.prev_char,mario)
                        self.x+=1
                        board.print_player(self.x,self.y,'P',mario)
                        self.prev_char=self.adv_char
                elif ((board.grid[self.x+2][self.y]=='X')):
                    self.adv_char=board.grid[self.x+1][self.y]
                    if self.adv_char=='P':
                        if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                            self.adv_char='H'
                        else:
                            self.adv_char=' '
                    board.print_player(self.x,self.y,self.prev_char,mario)
                    self.x+=1
                    board.print_player(self.x,self.y,'P',mario)
                    self.prev_char=self.adv_char


            #if self.adv_char=='P':
                #self.adv_char=' '
        #Moving Left
        if(ch=='a' or ch=='A'):
            if( (board.checkWall(self.x,self.y-1)) and (board.grid[self.x+1][self.y-1]=='X' or board.grid[self.x+1][self.y-1]=='H') ):
                self.adv_char=board.grid[self.x][self.y-1]
                if self.adv_char=='P':
                    if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                        self.adv_char='H'
                    else:
                        self.adv_char=' '
                if self.adv_char=='C':
                    self.adv_char=' '
                board.print_player(self.x,self.y,self.prev_char,mario)
                self.y-=1
                board.print_player(self.x,self.y,'P',mario)
                self.prev_char=self.adv_char
            if self.prev_char=='O':
                self.prev_char=' '


            #if self.adv_char=='P':
                #self.adv_char=' '
        #Moving right
        if(ch=='d' or ch=='D'):
            if( (board.checkWall(self.x,self.y+1)) and (board.grid[self.x+1][self.y+1]=='X' or board.grid[self.x+1][self.y+1]=='H') ):
                self.adv_char=board.grid[self.x][self.y+1]
                if self.adv_char=='P':
                    if ( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )):
                        self.adv_char='H'
                    else:
                        self.adv_char=' '
                if self.adv_char=='C':
                    self.adv_char=' '
                board.print_player(self.x,self.y,self.prev_char,mario)
                self.y+=1
                board.print_player(self.x,self.y,'P',mario)
                self.prev_char=self.adv_char
            if self.prev_char=='O':
                self.prev_char=' '

		#board.print_matrix()

            #if self.adv_char=='P':
                #self.adv_char=' '


    def jump(self,board,mario):
            if (self.x==4 and (self.y<=32 and self.y>=18)):
                board.print_player(self.x,self.y,'P',mario)
                self.stage=0
                return
            if self.stage==1:
                print "Enter direction: ( <--: a/A/ :  : d/D :--> )"
                self.jump_dir=getchar()
            if ((self.jump_dir=='d' or self.jump_dir=='D')):#Jump right
                if ((self.stage==1)  and (((self.y)+4)<=78) and (board.grid[self.x+1][self.y+4]!=' ')) :
                    self.adv_char=board.grid[self.x-1][self.y+1]
                    self.prev_char=' '
                    if board.grid[self.x-1][self.y]=='H' or board.grid[self.x-2][self.y]=='H':#Standing at the base of a staircase
                        self.prev_char='H'
                    self.x-=1
                    self.y+=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x+1,self.y-1,self.prev_char,mario)
                    self.prev_char=self.adv_char
                    board.print_matrix()
                    self.updatestage(board)
                    #time.sleep( 0.5 )

                elif ((self.stage==2) and (((self.y)+3)<=78) and (board.grid[self.x+2][self.y+3]!=' ')):
                    self.adv_char=board.grid[self.x-1][self.y+1]
                    self.x-=1
                    self.y+=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x+1,self.y-1,self.prev_char,mario)
                    os.system("clear")
                    board.print_matrix()
                    self.prev_char=self.adv_char
                    self.updatestage(board)
                    #os.system('clear')
                    #board.print_matrix()
                    #time.sleep( 0.5 )

                elif ((self.stage==3) and (((self.y)+2)<=78) and (board.grid[self.x+3][self.y+2]!=' ')):
                    self.adv_char=board.grid[self.x+1][self.y+1]
                    self.x+=1
                    self.y+=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x-1,self.y-1,self.prev_char,mario)
                    os.system("clear")
                    self.prev_char=self.adv_char
                    board.print_matrix()
                    self.updatestage(board)

                    #os.system('clear')
                    #board.print_matrix()
                    #time.sleep( 0.5 )

                elif ((self.stage==4)) :
                    self.adv_char=board.grid[self.x+1][self.y+1]
                    self.x+=1
                    self.y+=1
                    if self.adv_char=='O':
						#ADDITIONAL CHECK FOR FIREBALL COLLISION!!
						os.system("clear")
						print "Beware of the fireballs!"
						time.sleep(0.5)
						board.print_player(self.x-1,self.y-1,' ',mario)
						board.print_player(28,2,'P',mario)
						self.x=28
						self.y=1
						self.life-=1
						self.score-=25
						board.grid[28][1]=' '
						board.grid[27][0]='X'
						board.print_matrix()
						#End Check
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x-1,self.y-1,self.prev_char,mario)
                    self.prev_char=self.adv_char
                    self.updatestage(board)
                    #os.system('clear')
                    board.print_matrix()
                    if self.prev_char=='C':
                        board.collectCoin(self.x,self.y,mario)
                        self.prev_char=' '
                        self.score-=5
                else:
                    self.stage=0

            elif ( ( self.jump_dir=='a' or self.jump_dir=='A' ) ):#Jump left
                if(( self.stage==1) and ( (self.y-4)>=1 ) and ( board.grid[self.x+1][self.y-4]!=' ' ) ):
                    self.adv_char=board.grid[self.x-1][self.y-1]
                    self.prev_char=' '
                    if board.grid[self.x-1][self.y]=='H' or board.grid[self.x-2][self.y]=='H':#Standing at the base of a staircase
                        self.prev_char='H'
                    self.x-=1
                    self.y-=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x+1,self.y+1,self.prev_char,mario)
                    os.system('clear')
                    self.prev_char=self.adv_char
                    board.print_matrix()
                    self.updatestage(board)

                elif ((self.stage==2) and ( (self.y-3)>=1 ) and ( board.grid[self.x+2][self.y-3]!=' ' )):
                    self.adv_char=board.grid[self.x-1][self.y-1]
                    self.x-=1
                    self.y-=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x+1,self.y+1,self.prev_char,mario)
                    os.system('clear')
                    self.prev_char=self.adv_char
                    board.print_matrix()
                    self.updatestage(board)

                elif ((self.stage==3) and ( (self.y-2)>=1 ) and ( board.grid[self.x+3][self.y-2]!=' ' )):
                    self.adv_char=board.grid[self.x+1][self.y-1]
                    self.x+=1
                    self.y-=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x-1,self.y+1,self.prev_char,mario)
                    self.prev_char=self.adv_char
                    os.system('clear')
                    board.print_matrix()
                    self.updatestage(board)

                elif ((self.stage==4)):
                    self.adv_char=board.grid[self.x+1][self.y-1]
                    self.x+=1
                    self.y-=1
                    board.print_player(self.x,self.y,'P',mario)
                    board.print_player(self.x-1,self.y+1,self.prev_char,mario)
                    self.prev_char=self.adv_char

                    if self.adv_char=='O':#ADDITIONAL CHECK FOR FIREBALL COLLISION!!
                        os.system("clear")
                        print "Beware of the fireballs!"
                        time.sleep(0.5)
                        board.print_player(self.x-1,self.y-1,' ',mario)
                        board.print_player(28,2,'P',mario)
                        self.x=28
                        self.y=1
                        self.life-=1
                        self.score-=25
                        board.grid[28][2]=' '
                        board.grid[27][0]='X'
                        board.print_matrix()
                    os.system('clear')
                    board.print_matrix()
                    self.updatestage(board)
                    if self.prev_char=='C':
                        board.collectCoin(self.x,self.y,mario)
                        self.prev_char=' '
                        self.score-=5
                else:
                    self.stage=0

    def updatestage(self,board):
        self.stage+=1

    def getX(self):
        return self.x

    def getY(self):
        return self.y
