n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
a,b=0,0
if 1<=n and n<=100 and 1<=m and m<=100:
	A.sort()
	B.sort()
	print(int(A[n-1]),int(B[m-1]))