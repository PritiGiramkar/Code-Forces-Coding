n=int(input())
ls=list(map(int,input().split()))
dc={}
cnt=0
lg,gg=0,0
for i in ls:
	for j in ls:
		if j<i and lg==0:
			lg=1
		if j>i and gg==0:
			gg=1
		#print(ls,gg)
	if lg==1 and gg==1:
		if i in dc:
			dc[i]+=2
		else:
			dc[i]=2
	lg,gg=0,0
#print(dc)	
for i in dc.keys():
	if dc[i]==2:
		cnt+=1
print(cnt)