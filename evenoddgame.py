n=int(input())
win=1
if 1<=n and n<=pow(10,9):
	if (n%2==0):
		win=0
	elif n%3==0 or n==1:
		win=1
	else:
		win=1
	if win==0:
		print("Mahmoud")
	else:
		print("Ehab")