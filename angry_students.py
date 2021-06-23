t=int(input())
for i in range(t):
	n=int(input())
	s1=str(input()).upper()
	tup=tuple(s1)
	ls=list(tup)
	cnt,temp=0,0
	for i in range(n):
		if ls[i]=='A':
			for j in range(i+1,n):
				if ls[j]=='P':
					cnt+=1
				else:
					if ls[j]=='A':
						break
			if(cnt>temp):
				temp=cnt
			cnt=0
	print(temp)