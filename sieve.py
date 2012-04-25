#My first python program 
#Sieve of eratosthenes - Find's primes in range 2 to N
#N will be input by the user
N=int(input("Enter a value N:"))
isPrime=[1]*N
primes = []
i=2
while((i*i)<N):
	if(isPrime[i]):
		j=i+i
		while(j<N):
			isPrime[j]=0
			j=j+i
	i=i+1
for i in range(2,N):
	if(isPrime[i]):
		primes.append(i)
print primes
