n,k,t=map(int,input().split())
if 1<=n and n<=pow(10,9) and 1<=k and k<=n and 1<=t and t<=n+k:
	if t<=n:
		if t<=k:
			print(t)
		else:
			print(k)
	else:
		if t<=n+k:
			print((n+k)-t)