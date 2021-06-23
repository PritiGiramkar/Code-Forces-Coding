n=int(input())
home=input()
ls=[]
cnt=0
for i in range(n):
	str1=input()
	if str1.find(home)>=0:
		cnt+=1
if cnt==n and cnt%2==0:
	print("home")
else:
	print("contest")
