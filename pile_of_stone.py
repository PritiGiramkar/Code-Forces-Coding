n=int(input())
s1=str(input())
sum=0
for i in range(n):
	if s1[i]=='-' and sum>0:
		sum-=1
	else:
		if s1[i]=='+':
			sum+=1
print(sum)