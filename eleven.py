n=int(input())
ls=[]
a,b=0,1
i=0
s1=""
while(True):
	if i==0:
		ls.append(0)
	elif i==1:
		ls.append(1)
	else:
		result=ls[i-2]+ls[i-1]
		if result<=n:
			ls.append(result)
		else:
			break
	i+=1
for j in range(1,n+1):
	if j in ls:
		s1+='O'
	else:
		s1+='o'
print(s1)