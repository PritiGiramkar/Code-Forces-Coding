n,k=map(int,input().split())
v=1
if n<k:
	print(n)
elif n==k:
	print(n)
elif n==0:
	print(0)
elif k==1:
	print(n)
else:
	while True:
		while True:
			if v%k==0:
				break
			else:
				v+=1
		x=v
		sum=0
		while True:
			if x==1 or x==0:
				break
			else:
				sum+=x
				x=x//k
		sum+=x
		if sum>=n:
			break
		else:
			v+=1
	print(v)