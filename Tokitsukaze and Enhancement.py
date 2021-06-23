n=int(input())
cnt=0
ds={1:'A',3:'B',2:'C',0:'D'}
if n%4==1:
	print(0,ds[1])
elif n%4==2:
	print(1,ds[3])
elif n%4==3:
	print(2,ds[1])
else:
	print(1,ds[1])