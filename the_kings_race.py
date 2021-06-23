n=int(input())
r,c=map(int,input().split())
wr,wc,br,bc=1,1,n,n
fw,fb=0,0
if wr==r and wc==c:
	print("White")
elif br==r and bc==c:
	print("Black")
else:
	while True:
		wr+=1
		wc+=1
		if abs(wr-r)<=1 and abs(wc-c)<=1:
			fw=1
			break
		br-=1
		bc-=1
		if abs(br-r)<=1 and abs(bc-c)<=1:
			fb=1
			break
	if fw==1:
		print("White")
	else:
		print("Black")