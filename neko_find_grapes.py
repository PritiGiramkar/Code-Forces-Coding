c,k=map(int,input().split())
chest=list(map(int,input().split()))
keys=list(map(int,input().split()))
chest.sort()
keys.sort()
even_c,odd_c=0,0
even,odd=0,0
for i in range(c):
	if chest[i]%2!=0:
		odd_c+=1
	else:
		even_c+=1
	
for j in range(k):
	if keys[j]%2!=0:
		odd+=1
	else:
		even+=1
print(min(odd,even_c)+min(even,odd_c))