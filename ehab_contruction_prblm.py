n=int(input())
a,b=0,0
found=False
if n>=1 and n<=100:
	for i in range(1,n+1):
		for j in range(1,n+1):
			if j%i==0 and j*i>n and j//i<n:
				a,b=j,i
				found=True
				break
		if found:
			break
			
	if found:
		print(a,b)
	else:
		print(-1)