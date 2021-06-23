for i in range(int(input())):
	n=input()
	sum=0
	tup=tuple(n)
	for k in tup:
		sum+=int(k)
	print(sum)