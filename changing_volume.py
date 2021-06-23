t=int(input())
for i in range(t):

	a,b=map(int,input().split())
	cnt=0
	diff=abs(a-b)
	rem=diff//5
	diff-=(5*rem)
	cnt+=rem

	rem=diff//2
	diff-=(2*rem)
	cnt+=rem

	cnt+=diff
	print(cnt)