n,v=map(int,input().split())
diff=(n-v)+1
sum=v
if n>v:
	for i in range(2,diff):
		sum+=i
	print(sum)
else:
	print(n-1)