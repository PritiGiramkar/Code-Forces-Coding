a=int(input())
b=int(input())
c=int(input())
Lm,Ap,PE=0,0,0
if 1<=a and a<=1000 and 1<=b and b<=1000 and 1<=c and c<=1000:
	for i in range(1,a+1):
		if i*2<=b and i*4<=c:
			Lm,Ap,PE=i,i*2,i*4
		else:
			break
	print(Lm+Ap+PE)
			