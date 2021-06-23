n,m,k=map(int,input().split())
ls=list(map(int,input().split()))
p=1000000
love=0
for i in range(len(ls)):
	if ls[i]!=0 and ls[i]<=k and abs(m-1-i)<p and i!=(m-1):
		p=abs(m-1-i)
print(p*10)		