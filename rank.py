n=int(input())
ls=[]
ls2=[]
for i in range(n):
	ls=list(map(int,input().split()))
	result=sum(ls)
	ls.clear()
	ls2.append(result)
result2=max(ls2)
print(len(ls2)-1-ls2[::-1].index(result2)+1)		