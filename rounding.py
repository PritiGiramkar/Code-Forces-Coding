n=int(input())
if n%10!=0:
	s1=str(n)
	s=tuple(s1)
	last=int(s[len(s1)-1])
	if last<=5:
		while n%10!=0:
			n-=1
	else:
		while n%10!=0:
			n+=1
	print(n)
else:
	print(n)