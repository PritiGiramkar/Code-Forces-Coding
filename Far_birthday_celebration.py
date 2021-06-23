n=int(input())
r=[0]*n
c=[0]*n
#print(r,c)
for i in range(n):
	str1=input()
	for j in range(n):
		if str1[j]=='C':
			c[j]+=1
			r[i]+=1
#print(r,c)
sum=0
for i in range(n):
	if r[i]==2:
		sum+=1
	else:
		num,rum=1,1
		if r[i]>2:
			for j in range(1,r[i]+1):
				num*=j
			for k in range(1,r[i]-1):
				rum*=k
			avg=num//rum
			avg//=2
			sum+=avg
			#print(sum)
for i in range(n):
	if c[i]==2:
		sum+=1
	else:
		num,rum=1,1
		if c[i]>2:
			for j in range(1,c[i]+1):
				num*=j
			for k in range(1,c[i]-1):
				rum*=k
			avg=num//rum
			avg//=2
			sum+=avg
			#print(sum)
print(sum)