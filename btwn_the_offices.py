n=int(input())
s=input()
cnt=0
'''if 2<=n and n<=100:
	for i in range(n):
		if s[i]=='F':
			if i+1<n:
				if s[i+1]=='S':
					cnt-=1
				if s[i+1]=='F':
					cnt+=1
			else:
					break
		if s[i]=='S':
			if i+1<n:
				if s[i+1]=='S':
					cnt-=1
				if s[i+1]=='F':
					cnt+=1
			else:
					break
if cnt>0:
	print("YES")
else:
	print("NO")
'''
if s.count('SF')>s.count('FS'):
	print("YES")
else:
	print('NO')