def distance(v1, v2):
	l = len(v1)
	dis = 0
	for i in range(l-1):
		dis+= (v1[i]-v2[i])**2
	return dis	

def cmpr(x,y):
	if x[1] < y[1] :
		return -1
	elif x[1] > y[1]:
		return 1
	return 0

def KNNPredict(training, v, K):
	l = len(v)
	if( len(training[0]) <> l+1):
		print "Error! Feature mismatch"
	dist = []
	for example in training:
		dist.append((example,distance(example, v)))
	dist.sort(cmpr)		
	print dist
	print "\n"		
	votes = {}
	for i in range(K):		
		print dist[i][0][-1], " gets +1"
		votes[dist[i][0][-1]]=1+votes.get(dist[i][0][-1],0)
	
	print votes
	
	ans = -1
	bestvotes = 0
	for k,v in votes.iteritems():	
		if v > bestvotes:
			v = bestvotes
			ans = k
	return ans		
	
trainingSet = []
N = 0
N = int(input())
print "Taking in ", N ," trainig vectors"

for i in range(N):
	trainingSet.append([int(i) for i in raw_input().split(",")] )

print "Enter test-vector"
testVector = [int(i) for i in raw_input().split(",")]
print KNNPredict(trainingSet, testVector, 3)
