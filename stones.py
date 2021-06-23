t=int(input())
for i in range(t):
	a,b,c=map(int,input().split())
	cnt=0
	if 0<=a and 0<=b and 0<=c and a<=100 and b<=100 and c<=100:
		while True:
			if b>=1 and c>=2:
				b-=1
				c-=2
				cnt+=3
			elif a>=1 and b>=2:
				a-=1
				b-=2
				cnt+=3
			else:
				break
		print(cnt)