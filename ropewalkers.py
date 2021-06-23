*ls,d=map(int,input().split())
#print(ls,d)
ls.sort()
x=abs(ls[0]-ls[1])
y=abs(ls[1]-ls[2])
z=abs(ls[0]-ls[2])
v1,v2,v3=0,0,0
if x<d:
	v1=d-x
if y<d:
	v2=d-y
if z+v1<d:
	v3=d-(z+v1)
print(v1+v2+v3)
