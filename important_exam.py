n,m=map(int,input().split())
s=[input() for x in range(n)]
marks=list(map(int,input().split()))

f=0
for i in range(m):
	ls=[]
	for j in s:
		ls.append(j[i])
	l=set(ls)
	mx=max([ls.count(x) for x in l])
	f+=mx*marks[i]
print(f)