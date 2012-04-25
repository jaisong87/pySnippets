#P2 - Just checking out 2D Lists to become familiar with lists
#Construct a 2D list and print it

#constructing list of list
TwoDList = []
for i in range(0,10):
	list = []
	for j in range(1,11):
		list.append(i*10+j)
	TwoDList.append(list)

#printing list of list
for row in TwoDList:
	print row	
