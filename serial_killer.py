vic1,vic2=map(str,input().split())
n=int(input())
print(vic1,vic2)
for i in range(n):
	str1,str2=map(str,input().split())
	if str1==vic1:
		vic1=str2
	if str1==vic2:
		vic2=str2
	print(vic1,vic2)