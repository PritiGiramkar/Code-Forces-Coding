import math
t=int(input())
for i in range(t):
	n=int(input())
	ls=list(map(int,input().split()))
	product=1
	for j in ls:
		product*=j
	sqroot=math.sqrt(product)
	sqroot=str(sqroot)
	ind=sqroot.find('.',1)
	if sqroot[ind+1]=='0':
		print("NO")
	else:
		print("YES")