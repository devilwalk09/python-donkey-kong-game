#!/bin/usr/python
import matrix
import person
from person import *
board=matrix.Matrix()

class Donkey(Person):
    def __init__(self,x,y):
        self.__x=x # X,y coordinate of Donkey Kong is protected
        self.__y=y
        self.flagc=0
        self.flagh=0
        self.counter=1
        self.prev_char=' '

    def move(self,r_j,board,d):
        board.print_donkeykong(self.__x,self.__y,self.prev_char,d)
        if(r_j == 1): #If the random direction chosen is 'right'
            if(board.checkWall(self.__x,self.__y+1) and (board.grid[self.__x+1][self.__y+1]=='X' or board.grid[self.__x+1][self.__y+1]=='H')): #If the next point is not a wall
                self.__y+=1
        else:
            if(board.checkWall(self.__x,self.__y-1)  and (board.grid[self.__x+1][self.__y-1]=='X' or board.grid[self.__x+1][self.__y-1]=='H') ):
                self.__y-=1
        board.print_donkeykong(self.__x,self.__y,'D',d)
        self.counter+=1


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
