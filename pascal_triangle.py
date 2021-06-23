n=int(input(""))
for i in range(n):
	for j in range(i,n):
		print(end=" ")
	result=str(pow(11,i))
	for k in result:
		print(k,end=" ")
	print()