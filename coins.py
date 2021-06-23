n,S=map(int,input().split())
if 1<=n and n<=100000 and 1<=S and S<=pow(10,9):
	cnt=0
	if n==1:
		print(S)
	else:
		if S%n==0:
			print(S//n)
		else:
			print((S//n)+1)