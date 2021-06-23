str1=input()
if len(str1)>=3:
	tup=tuple(set(str1))
	
		ds={}
		for i in tup:
			ds[i]=0
		for i in str1:
			ds[i]+=1
		