n=int(input())
s=set(map(int,input().split()))
ls=list(s)
zero=ls.count(0)
if zero>0:
	print(len(ls)-1)
else:
	print(len(ls))