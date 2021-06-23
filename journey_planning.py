n=int(input())
ls=list(map(int,input().split()))
sum=0
for i in range(2,n+1):
	for j in range(1,i):
		if abs(i-j)==abs(ls[i-1]-ls[j-1]):
			sum+=i-j
print(sum)