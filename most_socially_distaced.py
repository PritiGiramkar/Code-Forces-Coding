for _ in range(int(input())):
	n=int(input())
	ls=list(map(int,input().split()))
	ls1=[]
	ls1.append(ls[0])
	for i in range(1,n-1):
		if (ls[i]>ls[i-1] and ls[i]>ls[i+1]) or (ls[i]<ls[i-1] and ls[i]<ls[i+1]):
			ls1.append(ls[i])
	ls1.append(ls[n-1])
	print(len(ls1))
	print(*ls1)