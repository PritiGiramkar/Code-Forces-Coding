#code
t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    sum=0
    while True:
        if len(ls)>1:
            #print(ls)
            m=max(ls)
            l=ls.count(m-1)
            if l!=0:
                ls.remove(m-1)
            sum+=m
            ls.remove(m)
        else:
            break
    if len(ls)!=0:
        sum+=ls.pop()
    print(sum)