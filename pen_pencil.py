t=int(input())
for j in range(t):
	a,b,c,d,k=map(int,input().split())
	pen,pencil=0,0
	if a<=c:
		pen=1
	else:
		i=1
		while(True):
			if a<=c*i:
				pen+=i
				break
			else:
				i+=1
	if b<=d:
		pencil=1
	else:
		i=1
		while(True):
			if b<=d*i:
				pencil+=i
				break
			else:
				i+=1
	if pen+pencil<=k:
		print(pen,pencil)
	else:
		print(-1)