#  !/bin/usr/python
from matrix import *
from player import *
from donkey import *
from fireball import *
rows,columns = 30,80
import os
import time

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

def main():

	keyslist=['a','A','s','S','d','D','w','W',' ','q','Q']
	"""Game Execution Starts here: """
	board = Matrix()
	checkboard = Matrix()
	x=28
	y=2
	mario=Player(x,y)

	donkeylist=[] #List of donkeys, number of donkeys increases for every level up to five
	donkeylist.append(Donkey(4,2))
	#donkeyobj=Donkey(4,2)
	board.print_player(x,y,'P',mario)
	board.print_donkeykong(4,2,'D',donkeylist[0])
	count=0
	os.system("clear")
	board.genCoins()
	board.print_matrix()
	r_j=random.randint(1,2)
	donkeylist[0].move(r_j,board,donkeylist[0]) #Move Donkey randomly
	fireballobj = []
	fireballobj.append(Fireball(donkeylist[0].getX(),donkeylist[0].getY()+1))

	print "Current Score: ", mario.scoreboard()
	counter=0
	i=0
	size=0

	while True:
		if mario.stage==0:
			print "Enter Command :"
			ch=getchar()
			if ch==' ':
				mario.stage=1
		if((ch=='q') or (ch=='Q') or (mario.livesleft()<=0)):
			os.system("clear")
			print "GAME OVER!"
			break
		if ch in keyslist:
			if mario.getX()==1: #Player has reached the queen
				os.system("clear")
				print "Congrats, 1 UP"
				time.sleep(0.5)
				mario.score+=50
				mario.level+=1
				mario.life=3
				board.print_player(mario.getX(),mario.getY(),' ',mario)
				mario.x=28
				mario.y=2

				for item in fireballobj:
						fireballobj.remove(item)

				fireballobj = []
				fireballobj.append(Fireball(donkeylist[0].getX(),donkeylist[0].getY()+1))

				for i in range(30):
					for j in range(80):
						if board.grid[i][j]=='O':
							if board.grid[i-1][j]=='H' or board.grid[i-2][j]=='H':
								board.grid[i][j]='H'
								board.print_player(i,j,'H',mario)
							else:
								board.grid[i][j]=' '
								board.print_player(i,j,' ',mario)

				if mario.level<=5: # MAX no of donkeys will be 5
					donkeylist.append(Donkey(4,2))
				os.system("clear")
				board.genCoins()
				board.print_matrix()
				#END OF RESET

			for item in fireballobj:#Check is fireballs have reached the bottom left corner
				if ((item.getX()==28) and (item.getY()==1)):
					board.print_player(item.getX(),item.getY(),' ',mario)
					fireballobj.remove(item)
			if (ch!=' '):
				mario.move(ch,board,mario) #Move Mario acc to input
			elif (ch==' '):
				mario.jump(board,mario)
				os.system("clear")
				board.print_matrix()
				#print "Mario Jump @stage in main", mario.stage
				print "Current Score: ", mario.scoreboard(), " ",
				print "Current Level: ", mario.levelreached(), " ",
				print "Lives Left: ", mario.livesleft()
				time.sleep(0.5)
				#mario.updatestage(board)
				if (mario.stage>4):
					mario.stage=0
			k=0
			for k in range(len(donkeylist)):
				r_j=random.randint(1,2)
				donkeylist[k].move(r_j,board,donkeylist[k]) #Move Donkey randomly
				board.checkDCollision(donkeylist[k],mario,ch)
				k+=1

			i=0
			for i in range(len(fireballobj)): # Fireballs only originate from the first donkey
				fireballobj[i].move(donkeylist[0],board,mario)
				ans=[0,0,0]
				ans=board.checkFCollision(fireballobj[i],mario,ch)
				if (ans[2]==1):
					if mario.onstair==1:
						if board.grid[ans[0]+1][ans[1]]!='X':
							board.print_player(ans[0]-1,ans[1],'H',mario)
						board.print_player(ans[0],ans[1],'H',mario)
						#os.system("CLEAR")
						#print "YES I AM ON STAIRS"
						#time.sleep(5)
						mario.collided=1
						board.print_matrix()
						board.grid[28][1]=' '
						i+=1

			counter+=1
			if ((counter%55)/mario.level)==0:#Number of Fireballs increases every level
				fireballobj.append(Fireball(donkeylist[0].getX(),donkeylist[0].getY()+1))



			print ""
			os.system("clear")
			board.print_matrix()
			print "Current Score: ", mario.scoreboard(), " ",
			print "Current Level: ", mario.levelreached(), " ",
			print "Lives Left: ", mario.livesleft()
		else:
			pass
			os.system("clear")
			board.print_matrix()
			print "Current Score: ", mario.scoreboard(), " ",
			print "Current Level: ", mario.levelreached(), " ",
			print "Lives Left: ", mario.livesleft()

if __name__=="__main__":
	main()
