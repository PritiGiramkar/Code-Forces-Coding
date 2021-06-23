n=int(input())
s1=input()
zero=s1.count('0')
ones=s1.count('1')
#print(zero,ones)
inzero=s1.find('0',zero)
inone=s1.find('1',ones)
#print(inzero,inone)
if n==1:
	print(1)
	print(n)
else:
	print(2)
	if inzero==-1:
		inzero=0
	if inone==-1:
		inone=0
	minval=min(inzero,inone)
	#print(minval)
	print(s1[:minval+1],s1[minval+1:])
