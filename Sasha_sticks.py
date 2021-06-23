n,k=map(int,input().split())
status=0
if 1<=n and n<=pow(10,18) and k<=n and 1<=k and k<=pow(10,18):
	ans=n//k
	if ans%2==0:
		print('NO')
	else:
		print('YES')