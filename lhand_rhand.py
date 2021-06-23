l,r,a=map(int,input().split())
if a==0 and (l==0 or r==0):
	print(0)
else:
	while a>0:
		if l<r:
			l+=1
		else:
			r+=1
		a-=1
	print(min(l,r)*2)