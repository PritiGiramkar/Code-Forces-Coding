n=int(input())
for i in range(0,n):
	candy=map(int,input())
	case=list(map(int,input().split()))
	if sum(case)%2==0:
		total=case.count(1)+case.count(2)
		if total%2==0:
			print("YES")
		else:
			if case.count(2)%2!=0 and case.count(1)%2==0:
				print("YES")
			else:
				print("NO")		
	else:
		print("NO")