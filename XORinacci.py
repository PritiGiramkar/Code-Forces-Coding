t=int(input())
if t>=1 and t<=pow(10,3):
	for j in range(t):
		a,b,n=map(int,input().split())
		ls=[]
		ls.append(a)
		ls.append(b)
		n%=3
		if n==0:
			print(a)
		elif n==1:
			print(b)
		else:
			print(a^b)