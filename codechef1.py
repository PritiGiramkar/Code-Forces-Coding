t=int(input())
for i in range(t):
	ls=list(map(int,input().split()))
	ls.sort()
	p,q,cnt=int(ls[0]),int(ls[1]),0
	while True:
		if q<=0:
			break
		else:
			q=q-p
			cnt+=1
	print(cnt)