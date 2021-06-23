for _ in range(int(input())):
	n=int(input())
	ls1=list(map(int,input().split()))
	ls2=list(map(int,input().split()))
	if (ls1==sorted(ls1)) or (0 in ls2 and 1 in ls2):
		print("Yes")
	else:
		print("No")