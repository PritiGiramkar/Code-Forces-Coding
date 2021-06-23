n=int(input())
a,b,c=0,0,0
flag=False
for i in range(n):
	if i%3!=0:
		for j in range(n):
			if j%3!=0:
				for k in range(n):
					if k%3!=0:
						if (i+j+k)==n:
							a,b,c=i,j,k
							flag=True
							break
			if flag==True:
				break
print(a,b,c)