def oddnum(n):
	sum1=0
	for j in range(1,n+1):
		if j%2!=0:
			sum1+=j
	return sum1
	
def calc(sum1):
	if sum1<10:
		return sum1
	else:
		sum1=list(tuple(str(sum1)))
		sum2=0
		flag=0
		for j in sum1:
			sum2+=int(j)
		#print(sum2)
		#print(*sum1)
		while sum2>9:
			sum2=0
			for j in sum1:
				sum2+=int(j)
			#print(sum2)
			sum1=list(tuple(str(sum2)))
	return sum2
str1=input()
#str1=str1.lower()
str1=list(tuple(str1))
ls=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(str1)):
	if str1[i] in ls:
		n=0
		n=i*5
		sum1=oddnum(n)
		#print(sum1)
		str1[i]=str(calc(sum1))
print("".join(str1))