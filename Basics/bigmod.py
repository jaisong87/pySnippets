#P3 - Calculate bigmod ( learn functions )
#bigmod - Calculates b**p % m
def bigmod(b, p, m):
	if(b==1):	
		return b%m 
	if(p==1):
		return b%m
	if(p%2==0):
		var1 = bigmod(b, p/2, m)
		var2 = (var1*var1)%m
		return var2
	var1 = bigmod(b, p-1,m)
	var2 = (var1*b)%m
	return var2


b = int(input("Enter b:"))
p = int(input("Enter p:"))
m = int(input("enter m:"))
print bigmod(b,p,m)
