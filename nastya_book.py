n=int(input())
ls=[]
for i in range(n):
	ls.append(list(map(int,input().split())))
#print(ls)
k=int(input())
total=n
for i in range(n):
		if k>ls[i][1]:
			total-=1
print(total)