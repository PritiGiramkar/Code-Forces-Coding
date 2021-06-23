n=int(input())
ls=list(map(int,input().split()))
d=0
pos=sum(1 for i in ls if i>0)
neg=sum(1 for i in ls if i<0)
num=0
if n%2==0:
	num=n//2
else:
	num=(n//2)+1

if pos>=num:
	print(1)
elif neg>=num:
	print(-1)
else:
	print(0)