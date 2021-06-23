n,m=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l2.sort()
l2.reverse()
for i in l1:
	if i in l2:
		print(i,end=" ")