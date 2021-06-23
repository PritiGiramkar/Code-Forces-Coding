for _ in range(int(input())):
	str1=input()
	ones=str1.count('1')
	zeros=str1.count('0')
	if ones==0 or zeros==0:
		print(str1)
	elif str1[0]=='0':
		str2="01"*((len(str1)//2)*2)
		print(str2)
	else:
		str2="10"*((len(str1)//2)*2)
		print(str2)