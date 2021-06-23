n=int(input())
ls1={"purple":"Power","green":"Time","blue":"Space","orange":"Soul","red":"Reality","yellow":"Mind"}
ls=[]
ls2=[]
cnt=0
for i in range(n):
	ls.append(str(input()).lower())
if "purple" not in ls:
	ls2.append("purple")
	cnt+=1
if "green" not in ls:
	ls2.append("green")
	cnt+=1
if "blue" not in ls:
	ls2.append("blue")
	cnt+=1
if "orange" not in ls:
	ls2.append("orange")
	cnt+=1
if "red" not in ls:
	ls2.append("red")
	cnt+=1
if "yellow" not in ls:
	ls2.append("yellow")
	cnt+=1
print(cnt)
for i in ls2:
	print(ls1[i])

	
