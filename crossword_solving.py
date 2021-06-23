n,m=map(int,input().split(' '))
s=str(input())
t=str(input())
f=-1
ans=n+1
for i in range(m-n+1):
    count=0
    for j in range(n):
        if s[j]!=t[i+j]:
            count+=1
        
    if count<ans:
        ans=min(ans,count)
        #print(ans)
        f=i
 
print(ans)
for i in range(n):
    if s[i]!=t[f+i]:
        print(i+1, end=' ')