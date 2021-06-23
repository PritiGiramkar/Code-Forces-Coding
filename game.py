n=int(input())
num=list(map(int,input().split()))
num.sort()
if n%2!=0:
 v=n//2
else:
 v=(n//2)-1
print(num[v])