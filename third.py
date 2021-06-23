import math
t=int(input())
for i in range(0,t):
	n=str(input())
	if(n.isdigit()):
		while(True):
			sum=0
			for i in range(0,len(n)):
				sum+=int(n[i])
			if(math.gcd(int(n),sum)>1):
				print(n)
				break
			else:
				n=int(n)
				n+=1
				n=str(n)