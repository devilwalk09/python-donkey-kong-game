#!/bin/usr/python
import random
import sys
import os
import time
class Matrix():
    def __init__(self, rows=30, columns=80, matsymbol = ' '):
        self.rows = rows
        self.columns= columns
        self.collisonflag=0
        self.grid = [ [matsymbol] * 80 for _ in xrange(30) ] #Initialising the game board
        for i in range(30):
            for j in range(80):
                if i == 0 or i == 29 or j == 0 or j == 79:
                    self.grid[i][j]='X'
        self.grid[1][20]='X'
        self.grid[1][30]='X'
        self.grid[1][25]='Q'  #Initialise Princess's location

        for j in range(20,31):
            self.grid[2][j]='X' #Set the floor for the Princess

        for j in range(50):         #Floor 5
            self.grid[5][j]='X'

        for j in range(10,79):      #Floor 4
            self.grid[9][j]='X'

        for j in range(65):         #Floor 3
            self.grid[13][j]='X'

        for j in range(24,79):      #Floor 2
            self.grid[17][j]='X'

        for j in range(70):         #Floor 1
            self.grid[21][j]='X'

        for j in range(16,79):      #Floor 0
            self.grid[25][j]='X'

            """ Generate Ladders"""
        for i in range(2,5):        # Princess Ladder
            self.grid[i][23]='H'

        for i in range(5,9):        #Level 5
            self.grid[i][30]='H'
        for i in range(5,9):         #BROKEN
            self.grid[i][40]='H'
            self.grid[7][40]=' '

        for i in range(9,13):      #Level 4
            self.grid[i][45]='H'
        for i in range(9,13):       #BROKEN
            self.grid[i][20]='H'
            self.grid[11][20]=' '

        for i in range(13,17):      #Level 3
            self.grid[i][34]='H'
        for i in range(13,17):      #BROKEN
            self.grid[i][57]='H'
            self.grid[15][57]=' '

        for i in range(17,21):      #Level 2
            self.grid[i][56]='H'
        for i in range(17,21):      #BROKEN
            self.grid[i][32]='H'
            self.grid[19][32]=' '

        for i in range(21,25):      #Level 1
            self.grid[i][28]='H'
        for i in range(21,25):      #BROKEN
            self.grid[i][67]='H'
            self.grid[23][67]=' '

        for i in range(25,29):      #Level 0
            self.grid[i][66]='H'
        for i in range(25,29):      #BROKEN
            self.grid[i][23]='H'
            self.grid[27][23]=' '


#    def print_matrix(self):
#        """ Printing out the current matrix as it looks"""
#        for row in self.grid:
#            print ''.join(row)

    def print_matrix(self):
        i=0
        j=0
        for i in range(30):
            for j in range(80):
                if (self.grid[i][j]=='X'):
                    print ('\033[91m'+ 'X' + '\033[0m'),
                elif (self.grid[i][j]=='Q'):
                    print ('\033[95m'+ 'Q' + '\033[0m'),
                elif (self.grid[i][j]=='O'):
                    print ('\033[1;41m'+ 'O' + '\033[1;m'),
                elif (self.grid[i][j]=='P'):
                    print ('\033[94m'+ 'P' + '\033[0m'),
                elif (self.grid[i][j]=='H'):
                    print ('\033[92m'+ 'H' + '\033[0m'),
                elif (self.grid[i][j]=='D'):
                    print ('\033[1;43m'+ 'D' + '\033[0m'),
                elif (self.grid[i][j]=='C'):
                    print ('\033[1;33m'+ 'C' + '\033[0m'),
                else:
                    print self.grid[i][j],
            print ""


    def print_player(self,x,y,char,mario): #To decide where to place the player
        if self.grid[x][y]=='C' and char=='P':
            self.collectCoin(x,y,mario)
        self.grid[x][y]=char

    def print_donkeykong(self,x,y,char,donkeyobj): #To decide where to place the Donkey
        if (self.grid[x][y]!='P' or char!=' '):
            if (char=='D'):
                if(self.grid[x][y]=='C'):
                    donkeyobj.flagc=1
                elif(self.grid[x][y]=='H'):
                    donkeyobj.flagh=1
            self.grid[x][y]=char
        if (donkeyobj.flagc==1 and char==' '):
            if self.grid[x][y]=='P':
                self.collectCoin(x,y)
            else:
                self.grid[x][y]='C'
            donkeyobj.flagc=0
        elif (donkeyobj.flagh==1 and char==' '):
            self.grid[x][y]='H'
            donkeyobj.flagh=0

    def collectCoin(self,x,y,mario):  #Increments Score for every coin collected
		mario.score+=5

    def checkWall(self,x,y):   #Has the PERSON hit a wall?
        if(self.grid[x][y]=='X'):
            #Return FALSE if obj will hit a wall
            return False
        else:
            return True
    def checkDonkey(self,x,y):
        if self.grid[x][y]=='D':
            return False
        else:
            return True

    def genCoins(self):
        levels=[4,8,12,16,20,24,28]
        i=random.randint(21,40)
        while i >= 0:
            r_j=random.randint(0,78)
            r_i=random.choice(levels)
            if self.grid[r_i][r_j]=='C' and self.grid[r_i][r_j] !=' ':
                r_j+=1
            if self.grid[r_i+1][r_j]=='X' and self.grid[r_i][r_j]==' ':
                self.grid[r_i][r_j]='C'
                i-=1

    def checkDCollision(self,d,p,ch):
        if( ( p.getX()==d.getX() ) and ( p.getY()==d.getY() ) ):
            os.system("clear")
            print "FINAL SCORE: ", p.scoreboard()
            print "GAME OVER!"
            sys.exit()
        elif( ( p.getX()==d.getX() ) ):
            if( ( ( (p.getY()-1) == d.getY() ) and (ch=='D' or ch=='d') ) or (p.getY()+1) == d.getY() and (ch=='A' or ch=='a') ):
                os.system("clear")
                print "FINAL SCORE: ", p.scoreboard()
                print "GAME OVER!"
        elif( ( p.getY()==d.getY() ) ):
            if( ( ((p.getX()-1)==d.getX()) and (ch=='s'or ch=='S') ) or ( ((p.getX()+1)==d.getX()) and (ch=='w'or ch=='W')) ):
                os.system("clear")
                print "FINAL SCORE: ", p.scoreboard()
                print "GAME OVER!"

    def checkFCollision(self,f,p,ch):
        ans=[0,0,0]
        if( ( p.getX()==f.getX() ) and ( p.getY()==f.getY() ) ):
                os.system("clear")
                print "Beware of the fireballs!"
                time.sleep(1)
                ans[0]=f.getX()
                ans[1]=f.getY()
                ans[2]=1
                #self.print_player(28,2,'P',p)
                p.x=28
                p.y=1
                p.life-=1
                p.score-=25
                self.grid[28][1]=' '
                self.print_matrix()
                #p.prev_char=' '


        elif( p.getX()==f.getX() ):
            if( ( ( (p.getY()-1) == f.getY() ) and (ch=='D' or ch=='d') ) or (p.getY()+1) == f.getY() and (ch=='A' or ch=='a') ):
                os.system("clear")
                print "Beware of the fireballs!"
                time.sleep(1)
                ans[0]=f.getX()
                ans[1]=f.getY()
                ans[2]=1
                self.print_player(p.getX(),p.getY(),' ',p)
                #self.print_player(28,2,'P',p)
                p.x=28
                p.y=1
                p.life-=1
                p.score-=25
                self.grid[28][1]=' '
                self.print_matrix()
                #p.prev_char=' '

        elif( (p.getY())==(f.getY()) ):
            if( ( ((p.getX()-1)==f.getX()) and (ch=='s'or ch=='S') ) or ( ((p.getX()+1)==f.getX()) and (ch=='w'or ch=='W')) ):
                os.system("clear")
                print "Beware of the fireballs!"
                time.sleep(1)
                ans[0]=f.getX()
                ans[1]=f.getY()
                ans[2]=1
                self.print_player(p.getX(),p.getY(),' ',p)
                #self.print_player(28,2,'P',p)
                p.x=28
                p.y=1
                p.life-=1
                p.score-=25
                self.grid[28][1]=' '
                self.print_matrix()
                if p.onstair==1:
                    self.print_player(ans[0]+1,ans[1],'H',p)
        return ans
