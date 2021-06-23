for i in range(int(input())):
	D,d,A,B,C=map(int,input().split())
	cat=D*d
	if cat>=42:
		print(C)
	elif cat>=21:
		print(B)
	elif cat>=10:
		print(A)
	else:
		print(0)