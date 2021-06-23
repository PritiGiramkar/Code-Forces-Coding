for _ in range(int(input())):
	n=int(input())
	s=str(input())
	m,p=0,0
	ls=[]
	for i in s:
		if i=='L':
			m-=1
		elif i=='R':
			m+=1
		elif i=='U':
			p+=1
		else:
			p-=1
		ls.append([m,p])
	print(ls)
	ind,flag=0,0
	for i in range(0,n-1):
		if ls[n-1][0]==ls[i][0] and ls[n-1][1]==ls[i][1]:
			flag=1
			ind=i+2
	if flag==1:
		print(ind,n)
	elif ls[n-1][0]==0 and ls[n-1][1]==0:
		print(1,n)
	else:
		print(-1)			