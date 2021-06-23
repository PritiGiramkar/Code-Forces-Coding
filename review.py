t=int(input())
if 1<=t and t<=10**4:
	for i in range(t):
		u,d=0,0
		n=int(input())
		if 1<=n and n<=50:
			ls=list(map(int,input().split()))
			for i in ls:
				if i==1:
					u+=1
				elif i==2:
					d+=1
				elif i==3:
					if u>=d:
						u+=1
					else:
						d+=1
				else:
					continue
		print(u)