n,m=list(map(int,input().split()))
s=str(input()).lower()
s1=tuple(s)
s2=list(s1)
for i in range(m):
	l,r,c1,c2=list(map(str,input().split()))
	for j in range(int(l)-1,int(r)):
		if s2[j]==c1:
			s2[j]=c2
print("".join(s2))