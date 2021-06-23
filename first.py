n=int(input())
for i in range(0,n):
	case=list(map(int,input().split()))
	w,h=case[0],case[1]
	cnt,total=1,case[2]
	while w%2==0:
		w=w/2
		cnt*=2
	while h%2==0:
		h/=2
		cnt*=2
	if cnt>=total:
		print("YES")
	else:
		print("NO")
	

