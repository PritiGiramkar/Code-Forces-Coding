str1=input()
ls={'(':')','{':'}','[':']','<':'>'}
str2=[]
cnt=0
flag=0
for i in str1:
	if i in ls:
		str2.append(i)
	else:
		if len(str2)!=0:
			if ls[str2[-1]]==i:
				str2.pop()
			else:
				cnt+=1
				str2.pop()
		else:
			flag=1
			break
#print(cnt)
if len(str2)==0 and flag==0:
	print(cnt)
else:
	print('Impossible')