n=int(input())
s=input()
m=0
s1=set()
for i in s:
	if i.isupper():
		s1=set()
	else:
		s1.add(i)
		m=max(m,len(s1))
print(m)
