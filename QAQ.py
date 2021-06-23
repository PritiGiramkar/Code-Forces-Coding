s1=str(input())
cnt=0
for i in range(len(s1)):
	for j in range(i+1,len(s1)):
		for k in range(j+1,len(s1)):
			if s1[i]=='Q' and s1[j]=='A' and s1[k]=='Q':
				cnt+=1
print(cnt)