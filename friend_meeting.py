a=int(input())
b=int(input())
minval=min(a,b)
maxval=max(a,b)
diff=abs(a-b)
cnt=0
for i in range(1,diff+1):
	if minval==maxval:
		break
	minval+=1
	cnt+=i
	if minval==maxval:
		break
	maxval-=1
	cnt+=i
print(cnt)