ls=list(map(int,input().split()))
a,b,sum=0,0,0
for i in range(len(ls)):
	if int(ls[i])>0:
		print(i)
		a=i
		print(a)
		break
for j in reversed(range(len(ls))):
	if int(ls[j])>0:
		b=j
		print()
		break
ls2=[]
for k in range(a,b+1):
	ls2.append(ls[k])
ls2.sort()
print(ls2)
del ls2[0]
for m in ls2:
	sum+=m
print(sum)