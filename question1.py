#question 1

n,sum,i=32,0,0
while True:
	sum=sum+float(1/2**i)
	if 2**i==n:
		break
	i+=1
print("{:.2f}".format(sum))

'''
Output:
1.97
'''

'''
explanation:

1/2^0 + 1/2^1 + 1/2^2 + 1/2^3 +1/2^4 + 1/2^5

=1.97

'''