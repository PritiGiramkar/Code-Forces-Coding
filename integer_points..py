for i in range(int(input())):
	n=int(input())
	ls=list(map(int,input().split()))
	m=int(input())
	ls1=list(map(int,input().split()))
	en,on,em,om=0,0,0,0
	for i in ls:
		if i%2==0:
			en+=1
		else:
			on+=1
	for i in ls1:
		if i%2==0:
			em=em+1  
		else:
			om=om+1
	print((en*em)+(on*om))