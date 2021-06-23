n=int(input())
if n>=2 and n<=5000:
	A=list(map(int,input().split()))
	ls=[]
	i=1
	cnt=1
	ls.append(1)
	for i in range(n):
		if A[A[A[i]-1]-1]-1==i:
			print("YES")
			cnt=0
			break
	if cnt:
		print("NO")
			