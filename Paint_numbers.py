n=int(input())
ls=list(map(int,input().split()))
l=[]
c=0
cnt=0
while ls:
	j=min(ls)
	ls=[x for x in ls if x%j!=0]
	c+=1
print(c)