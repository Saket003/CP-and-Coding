import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

#To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)


#HELPER FUNCTIONS

#Returns the associated value for the uppercase alphabet (A to Z is mapped to 0 to 25)
def val(ch):
	return ord(ch)-65

#Time O(mlog(q))
#Both loops iterate m times with O(1) operations giving O(m) in absence of modulo
#With modulo, operations are of the order m*log(q) rather than m*1
#O(logq) space
def hash(q,str,m):
	h = 0 # Hash value
	key = 1 # Rehash key - (26^m-1)%q
	for i in range (0,m-1):
		key = (key*26)%q
	for i in range (0,m):
		h = ((26*h) + val(str[i]))%q
	return h,key

#Time O(mlogq)
#O(logq) space
def hash_excluded(q,str,m,index):
	h = 0 # Hash value
	key1 = 1 # Rehash key - (26^m-2)%q
	key2 = 1 # Rehash key - (26^m-i-2)%q
	for i in range (0,m-1):
		key1 = (key1*26)%q
	for i in range (0,m-index-1):
		key2 = (key2*26)%q
	for i in range (0,m):
		if(i!=index):
			h = ((26*h) + val(str[i]))%q
		else:
			h = ((26*h))%q
	return h,key1,key2

#Time O(logq)
#No additional storage - discards old so same O(logq)
def rehash(q,h,key,chi,chj): #Remove i, add j
	h = ((26*h)%q - (((26*(val(chi)))%q)*key)%q + val(chj)%q)%q
	while (h < 0):
		h = h + q
	return h

#Time O(logq)
#No additional storage
def rehash_excluded(q,h,key1,key2,chi,chj,chi2,chij2): #Remove i, add j
	h = ((26*h)%q - (((26*(val(chi)))%q)*key1)%q + val(chj)%q + (((26*(val(chi2)))%q)*key2)%q - (val(chij2)*key2)%q)%q
	while (h < 0):
		h = h + q
	return h


#ASSIGNMENT REQUIREMENTS

# return appropriate N that satisfies the error bounds
def findN(eps,m):
	n = m/eps
	factor = 2*math.log2(26)
	safety_factor = 1 #Optional - Can increase N if needed - Larger N reduces error
	N = int(safety_factor*factor*n*math.log2(n))
	return N

# Return sorted list of starting indices where p matches x
# Time O(m*logq + (n-m)*logq) and Space (logn+logq)
def modPatternMatch(q,p,x):
	m = len(p)
	n = len(x)
	indices = []

	hash_p,key = hash(q,p,m)
	hash_x,key = hash(q,x,m)
	for i in range(0,n-m+1):
		if(hash_p == hash_x):
			indices.append(i)
		if(i!=n-m):
			hash_x = rehash(q,hash_x,key,x[i],x[m+i])
	return indices


# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	m = len(p)
	n = len(x)
	indices = []
	index = p.find('?')

	hash_p,key1,key2 = hash_excluded(q,p,m,index)
	hash_x,key1,key2 = hash_excluded(q,x,m,index)
	for i in range(0,n-m+1):
		if(hash_p == hash_x):
			indices.append(i)
		if(i!=n-m):
			hash_x = rehash_excluded(q,hash_x,key1,key2,x[i],x[m+i],x[i+index],x[i+index+1])
	return indices

"""
Refer README.md for - 
	- Description
	- Inequality of pi(n)
	- Proof for findN
	- Time and Space Complexity Analysis

Copied here until assignment deadline passes :)
For a given i, for false positive,
	Pr[i belongs to L]
	= Pr[q|(f(x[i..(i + m - 1)]) - f(p))]
	= # of primes from 1 to N dividing (f(x[i..(i + m - 1)]) - f(p))  /  Total # of primes from 1 to N  ---(i)

	Total # of primes from 1 to N (pi(N)) is related by inequality:
	pi(N)>= N/2log(N)

	Substituting in (i),
	Pr[i belongs to L]
	<= # of primes from 1 to N dividing (f(x[i..(i + m - 1)]) - f(p))  /  (N/2log(N))  ---(ii)
	
	# of primes from 1 to N dividing (f(x[i..(i + m - 1)]) - f(p))
	Using Claim:
	The number of prime factors of a positive integer d is at most log(d).
	
	Substituting in (ii),
	Pr[i belongs to L]
	<= log(f(x[i..(i + m - 1)]) - f(p))*2log(N)/N  ---(iii)

	f(x[i..(i + m - 1)]) - f(p) is a 26-bit number with m digits, hence in decimal representation,
	f(x[i..(i + m - 1)]) - f(p) < 26^m - 1 < 26^m

	Substituting in (iii),
	Pr[i belongs to L]
	<= 2log(26)*m*log(N)/N

	Let N be of the form a*(m/eps)*log(m/eps),
	RHS = 2log(26)*m*log(a*m/eps*log(m/eps))  /  a*(m/eps)*log(m/eps)
		= 2log(26)*(eps/a)*(log(a) + log(m/eps) + log(log(m/eps)))  /  log(m/eps)
	For small eps,
	We know, log(x) >> log(log(x))
	Also for sufficiently small eps,
	m/eps >> a

	RHS = 2log(26)*(eps/a)*log(m/eps) /  log(m/eps)
		= (2log(26)/a)*eps
	Hence, by selecting a = 2log(26), we get
	Pr[i belongs to L] <= eps
	Which is the required condition
	
"""