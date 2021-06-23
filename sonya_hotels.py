n,d=map(int,input().split())
ls=list(map(int,input().split()))
c=2
#print(n,d)
if n==1:
	print(2)
else:
	for i in range(1,len(ls)):
		if abs(ls[i]-ls[i-1])==d*2:
			c+=1
		elif abs(ls[i]-ls[i-1])>d*2:
			c+=2
		else:
			continue
	print(c)