n=int(input())
if 1<=n and n<=pow(10,5):
	#if n%2==0 or n%3==0 or n%5==0:
	str1=input()
	one=str1.count('n')
	zero=str1.count('z')
	ls=[]
	if str1.count('o')==(one+zero):
		for i in range(one):
			ls.append('1')
		for j in range(zero):
			ls.append('0')
		print(" ".join(ls))
				