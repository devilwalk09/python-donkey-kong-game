#!/bin/usr/python
import random
import os
import time
class Fireball():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.adv_char=' '
        self.rdir=1
        self.take_what=1
        self.prev_char=' '

    def move(self,donkeyobj,board,mario):
        if(self.prev_char=='P'):
            if( (board.grid[self.x-1][self.y]=='H') or (board.grid[self.x-2][self.y]=='H') or ( (board.grid[self.x+1][self.y]=='H') and (board.grid[self.x][self.y+1]=='X')  )or (mario.onstair==1)):
                self.prev_char='H'
            else:
                #os.system("clear")
                #print "SELF.PREV=P"
                #time.sleep(3)
                self.prev_char=' '

        board.print_player(self.x,self.y,self.prev_char,mario)
        if self.rdir==1:
            # MOVE Right
            if(board.checkWall(self.x,self.y+1)): #If the next point is not a wall
                if ((board.grid[self.x+1][self.y+1]=='H') or (board.grid[self.x+1][self.y+1]==' ')):
                    self.rdir=3
                #if(self.adv_char)=='O':
                #    self.adv_char=' '
                self.adv_char=board.grid[self.x][self.y+1]
                if self.prev_char=='O':
                    #Check if the collision with another fireball happened at a staircase?
                    if board.grid[self.x-2][self.y]=='H':
                        self.prev_char='H'
                    else:
                        self.prev_char=' '

                board.print_player(self.x,self.y,self.prev_char,mario)
                self.y+=1
                board.print_player(self.x,self.y,'O',mario)
                self.prev_char=self.adv_char

            else:#Next point is a wall
                self.rdir=2
                board.print_player(self.x,self.y,'O',mario)

        elif self.rdir==2:
            # MOVE Left
            if(board.checkWall(self.x,self.y-1)):
                if ((board.grid[self.x+1][self.y-1]=='H') or (board.grid[self.x+1][self.y-1]==' ')):#If O is at the edge of a platform
                    self.rdir=3
                #if(self.adv_char)=='O':
                #    self.adv_char=' '
                self.adv_char=board.grid[self.x][self.y-1]
                if self.prev_char=='O':
                    #Check if the collision with another fireball happened at a staircase?
                    if board.grid[self.x-2][self.y]=='H':
                        self.prev_char='H'
                    else:
                        self.prev_char=' '

                board.print_player(self.x,self.y,self.prev_char,mario)
                self.y-=1
                board.print_player(self.x,self.y,'O',mario)
                self.prev_char=self.adv_char
            else:
                self.rdir=1
                board.print_player(self.x,self.y,'O',mario)

        elif self.rdir==3:
            # MOVE Down
            if board.grid[self.x+1][self.y]=='X':#Choose a random direction on falldown
                self.rdir=random.randint(1,2)

            if ((board.grid[self.x+1][self.y]=='H')):#Moving down on a staircase
                if ((board.grid[self.x+1][self.y+1]=='X') or (board.grid[self.x+1][self.y-1]=='X')):#First block of a staicase-XXHXX
                    self.take_what=random.randint(1,2)#decide whether to take the stairs
                if ((self.take_what == 1)): #TAKE THE staircase
                    #if(self.adv_char)=='O':
                        #self.adv_char=' '
                    self.adv_char=board.grid[self.x+1][self.y]
                    board.print_player(self.x,self.y,self.prev_char,mario)
                    self.x+=1
                    board.print_player(self.x,self.y,'O',mario)
                    self.prev_char=self.adv_char

                else:#IF NOT TAKING THE STAIRCASE
                    self.rdir=1#TRY MOVE RIGHT First
            elif ((board.grid[self.x+1][self.y]==' ') or (board.grid[self.x+1][self.y]=='C')):
                    self.adv_char=board.grid[self.x+1][self.y]
                    board.print_player(self.x,self.y,self.prev_char,mario)
                    self.x+=1
                    board.print_player(self.x,self.y,'O',mario)
                    self.prev_char=self.adv_char
    #    if self.x==28 and self.y==2:
    #                board.grid[self.x][self.y]=' '
    #                self.rdir=4

    def getX(self):
        return self.x

    def getY(self):
        return self.y
