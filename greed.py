n=int(input())
rem=sum(list(map(int,input().split())))
can=list(map(int,input().split()))
ls=[]
for i in can:
	for j in can:
		if i!=j:
			ls.append(i+j)
m=max(ls)
#print(ls)
print("YES") if m>=rem else print("NO")