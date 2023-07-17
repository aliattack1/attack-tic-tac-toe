







# tic tac toe v 1.0.0
'''
this is a simple tic tac toe 
player is x comouter is o 
computer places randomly(not logicaly)

numbering method
1	2	3
4	5	6
7	8	9


'''





#importing a random method for temp computer choice
from random import choice as r


#avoiding glass break in my device
print('\n'*5)
#list of x, o and un chosed places+ the top note
li=['-','-','-','-','-','-','-','-','-','welcome']




#the decorator for visualising table show
def shod(show):
	def iner(li):
		
		
		print('\n'*3)
		print('\t'+li[9])
		print('\t'+'#'*20)
		show(li)
		print('\t'+'#'*20)
		print('\n'*3)
		
		
		
	return iner

#the function to print the table
@shod
def show(li):
	print(f'\t{li[0]}\t{li[1]}\t{li[2]}\t')
	print(f'\t{li[3]}\t{li[4]}\t{li[5]}\t')
	print(f'\t{li[6]}\t{li[7]}\t{li[8]}\t')


#showing first time table
show(li)



#player turn 
def pturn(li):
	chose = int(input('\n the number of the chosen play'))
	if li[chose-1] == '-':
		li[chose-1]='x'
	return li


#checks if player had win
def chpwin(li):
	wintup=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
	for a in wintup:
		if li[a[0]-1] =='x':
			if li[a[1]-1] =='x':
				if li[a[2]-1] =='x':
					print('youwon')
					quit()
#checks if computer had win 
def chcwin(li):
	wintup=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
	for a in wintup:
		if li[a[0]-1] =='o':
			if li[a[1]-1] =='o':
				if li[a[2]-1] =='o':
					print('youlose')
					quit()
#checks free slots
def remain(li):
	rem = []
	n= 1
	for i in li[0:9]:
		if i=='-':
			rem+=[n]
		n+=1
	return rem

# temperetaory random computer turn
def cturn(li):
	a=remain(li)
	b=r(a)
	li[b-1]='o'
	return li


#main loop
while True:
	li=pturn(li)
	show(li)
	chpwin(li)
	li=cturn(li)
	show(li)
	chcwin(li)