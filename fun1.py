class A():
	__var1=3
	def __init__(self,var1,var2):
		self.__var1=var1
		self.var2=var2
	def printing(self):
		print(self.__var1,self.var2)
class C():
	def __init__(self,var4):
		self.var4=var4
	def printing(self):
		print(self.var4)
class B(A,C):
	def __init__(self,var1,var2,var3,var4):
		A.__init__(self,var1,var2)
		C.__init__(self,var4)
		self.var3=var3
	def printing(self):
		A.printing(self)
		C.printing(self)
		print(self.var3)

obj1=A(5,4)
obj3=C(10)
obj2=B(6,7,8,11)
obj1.printing()
obj3.printing()
obj2.printing()