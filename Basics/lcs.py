#P4 - lcs
#Computes lowest common subsequence of 2 strings
def lcs(X, Y):
	m=len(X)
	n=len(Y)
	lcsArr = []
	for i in range(m):
		row = [0]*n
		lcsArr.append(row)
	for i in range(m):
		for j in range(n):
			diag = 0
			if(i> 0 and j>0 ):
				diag = lcsArr[i-1][j-1]
			top = 0
			if(i):
				top = lcsArr[i-1][j]
			left = 0
			if(j):
				left = lcsArr[i][j-1]
			if(X[i]==Y[j]):
				lcsArr[i][j] = max(lcsArr[i][j], 1+diag)
			lcsArr[i][j] = max(lcsArr[i][j], left)
			lcsArr[i][j] = max(lcsArr[i][j], top)			
	return lcsArr[m-1][n-1]


X=raw_input("Enter first string:")
Y=raw_input("Enter second string:")
#print X, ",", len(X)
#print Y, "," , len(Y)
print "LCS (", X, ",", Y,") = ", lcs(X,Y)

