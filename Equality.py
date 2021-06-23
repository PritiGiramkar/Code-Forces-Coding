import string
s1=string.ascii_uppercase
n,k=map(int,input().split())
str1=str(input())
s=tuple(s1)
if n>=1 and n<pow(10,9) and k>=1 and k<=26:
	min1=str1.count(s[0])
	for i in range(1,k):
		min1=min(str1.count(s[i]),min1)
	print(min1*k)

