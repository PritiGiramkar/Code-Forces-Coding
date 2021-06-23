n,k=list(map(int,input().split()))
sum=0
red=int(n)*2
green=int(n)*5
blue=int(n)*8
if red%k==0:
	sum+=(red//k)
else:
	sum+=(red//k)+1
if green%k==0:
	sum+=(green//k)
else:
	sum+=(green//k)+1
if blue%k==0:
	sum+=(blue//k)
else:
	sum+=(blue//k)+1
print(sum)