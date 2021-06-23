for i in range(int(input())):
	n=int(input())
	ls=list(map(int,input().split()))
	ls1=[]
	sum=0
	if n==2:
		mul=str(ls[0]*ls[1])
		tup=tuple(mul)
		for i in tup:
			sum+=int(i)
		print(sum)
	else:
		for i in range(0,n-1):
			for j in range(i+1,n):
				sum=0
				val=str(ls[i]*ls[j])
				tup=tuple(val)
				for k in tup:
					sum+=int(k)
				ls1.append(sum)
		print(max(ls1))
		