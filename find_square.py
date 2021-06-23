n,m=map(int,input().split())
ls=[]
for i in range(n):
	ls.append(input())
for j in range(n):
	if 'B' in ls[j]:
		cnt=ls[j].count('B')
		ind=ls[j].index('B')
		break
row=j+cnt//2
col=ind+cnt//2
print(row+1,col+1)