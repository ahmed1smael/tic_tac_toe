#Copyright [2018] Ahmed Salman [ahmed.salman.iq@gmail.com] All rights reserved.

l=['0','1','2','3','4','5','6','7','8','9']
s='|'
print ("\n\n\n###\nHello! and welcome to my tic tac toe game (test game) \n\n\nIt's a multiplayer game and thus requires two players")
print ("please select any number from 0-9\n###\n\n\n\n")

def printing_welcome():
	print ('\t-------')
	print ('\t' + s + l[0] + s + l[1] + s + l[2] + s)
	print ('\t-------')
	print ('\t' + s + l[3] + s + l[4] + s + l[5] + s)
	print ('\t-------')
	print ('\t' + s + l[6] + s + l[7] + s + l[8] + s)
	print ('\t-------\n\n\n')

printing_welcome()

p1=''
m1=int
s1=range(0,9)
p2=''
m2=int
s2=range(0,9)
l1=['ais',2,0,1,8]
m=[0,1,2,3,4,5,6,7,8]
a=''

def player_one():
	global p1
	global s1
	global m1
	p1=input('player_1>')
	try:
			int(p1)
	except ValueError:
    		try:
        		float(p1)
    		except ValueError:
        		print ("This is not a number")
        		player_one()
	m1=int(p1)
	if m1 in s1:
		if l[m1]=='X' or l[m1]=='O':
			print ('\n\nerror : used , please select other available options')
			player_one()
		else:
			l[m1]='X'
			printing_welcome()
			winner1()

	else:
		print ('\n\nWARNING\n\nerror please select values between 0 and 9')
		player_one()

def player_two():
	global p2
	global s2
	global m2
	p2=input('player_2>')
	try:
    		int(p2)
	except ValueError:
    		try:
        		float(p2)
    		except ValueError:
        		print ("This is not a number")
        		player_two()

	m2=int(p2)
	if m2 in s2:
		if l[m2]=='X' or l[m2]=='O':
			print ('\n\nerror : used , please select other available options')
			player_two()
		else:
			l[m2]='O'
			printing_welcome()
			winner2()
	else:
		print ('\n\nWARNING\n\nerror please select values between 0 and 9')
		player_two()



def winner1():
	if l[m1]=='X' and l[0]==l[1] and l[0]==l[2]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[0]==l[4] and l[0]==l[8]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[0]==l[3] and l[0]==l[6]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[3]==l[4] and l[3]==l[5]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[6]==l[7] and l[6]==l[8]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[2]==l[4] and l[2]==l[6]:
		print ('winner is player_1')
		ask_again()
	elif l[m1]=='X' and l[2]==l[5] and l[2]==l[8]:
		print ('winner is player_1')
		ask_again()
	else:
		draw1()

def winner2():
	if l[m2]=='O' and l[0]==l[1] and l[0]==l[2]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[0]==l[4] and l[0]==l[8]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[0]==l[3] and l[0]==l[6]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[3]==l[4] and l[3]==l[5]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[6]==l[7] and l[6]==l[8]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[2]==l[4] and l[2]==l[6]:
		print ('winner is player_2')
		ask_again()
	elif l[m2]=='O' and l[2]==l[5] and l[2]==l[8]:
		print ('winner is player_2')
		ask_again()

	else:
		draw2()


def draw1():
	global m
	m.pop()
	if m==[]:
		print ('Its draw .... shame')
		ask_again()
	else:
		player_two()


def draw2():
	global m
	m.pop()
	if m==[]:
		print ('Its draw .... shame')
		ask_again()
	else:
		player_one()

def ask_again():
	global a
	a=input('Remach ? (yes/no) > ').lower().startswith('y')
	if a:
		reset_values()
		printing_welcome()
		player_one()
	else:
		exit()
	

def reset_values():
	global l,s,p1,p2,s2,m,a
	l=['0','1','2','3','4','5','6','7','8','9']
	su=['ais',2,0,1,8]
	s='|'
	p1=int
	s1=range(0,9)
	p2=int
	s2=range(0,9) 
	a=''
	m=[0,1,2,3,4,5,6,7,8]

player_one()




