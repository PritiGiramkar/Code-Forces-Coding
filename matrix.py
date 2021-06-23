import numpy as np

def calcrow(ls):
	arr=np.array(ls)
	sum1=arr.sum(axis=1)
	#print(sum1)
	return sum1

def calccol(ls):
	arr=np.array(ls)
	sum1=arr.sum(axis=0)
	#print(sum1)
	return sum1

n=int(input())
ls=[]
for _ in range(n):
	l1=list(map(int,input().split()))
	ls.append(l1)

rowlen=len(ls[0])
zero,other=0,0

for i in range(n):
	zero+=ls[i].count(0)
other=(n*rowlen)-zero
#print(zero,other)
flag=0

if zero>=other:
	for i in range(n):
		for j in range(rowlen):
			rowcount,colcount=calcrow(ls),calccol(ls)
			#print(rowcount,colcount)
			if ls[i][j]==0:
				if rowcount[i]<=colcount[j]:
					val=1
					while True:
						if (rowcount[i]+val)%2==0:
							ls[i][j]=val
							break
						else:
							val+=1
				else:
					val=1
					while True:
						if (rowcount[i]+val)%3==0:
							ls[i][j]=val
							break
						else:
							val+=1
				zero-=1
				other+=1
			if zero<other:
				flag=1
				break
		if flag==1:
			break
	print("------------")
	for i in range(n):
		print(*ls[i])
else:
	print(-1)
