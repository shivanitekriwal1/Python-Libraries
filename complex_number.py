import math

class complex_number(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def represent(self):
		if type(self.x)==int and type(self.y)==int:
			if self.y>=0:
				return '%d+%di'%(self.x, self.y)
			else: 
				return '%d%di'%(self.x, self.y)
		else:
			if self.y>=0:
				return '%.2f+%.2fi'%(self.x, self.y)
			else:
				return '%.2f%.2fi'%(self.x, self.y)


	def __add__(self, other):
		r1 = self.x
		i1 = self.y
		r2 = other.x
		i2 = other.y
		R = r1 + r2
		I = i1 + i2
		if (I<0):
			return (str(R)+str(I)+"i")
		else:
			return (str(R)+"+"+str(I)+"i")

	def __sub__(self, other):
		r1 = self.x
		i1 = self.y
		r2 = other.x
		i2 = other.y
		R = r1 - r2
		I = i1 - i2
		if (I<0):
			return (str(R)+str(I)+"i")
		else:
			return (str(R)+"+"+str(I)+"i")

	def __mul__(self, other):
		r1 = self.x
		i1 = self.y
		r2 = other.x
		i2 = other.y
		R = ((r1*r2) - (i1*i2))
		I = ((r1*i2) + (i1*r2))
		if (I<0):
			return (str(R)+str(I)+"i")
		else:
			return (str(R)+"+"+str(I)+"i")

	def __div__(self,other):
		r1 = self.x
		i1 = self.y
		r2 = other.x
		i2 = other.y

		try:
			R = float((r1*r2)+(i1*i2))/((r2*r2)+(i2*i2))
			I = float((i1*r2)-(r1*i2))/((r2*r2)+(i2*i2))
			if (I<0):
				return (str(R)+str(I)+"i")
			else:
				return (str(R)+"+"+str(I)+"i")
		except ZeroDivisionError:
			print " Denominator cannot be zero"

	def abs(self):
		r1 = float('%.2f'%(self.x))
		i1 = float('%.2f'%(self.y))
		return (((r1*r1)+(i1*i1))**(1/2.0))

	def real(self):
		r1 = float('%.2f'%(self.x))
		return ("real part of the complex number =" + str(r1))

	def imaginary(self):
		i1 = float('%.2f'%(self.y))
		return ("imaginary part of the complex number=" + str(i1))

	def argument(self):
		r1 = float('%.2f'%(self.x))
		i1 = float('%.2f'%(self.y))
		arg = math.degrees(math.atan(i1/r1))
		return arg

	def conjugate(self):
		r1 = '%.2f'%(self.x)
		i1 = '%.2f'%(self.y)
		if i1>=0:
			return (str(r1)+"-"+str(i1)+"i")
		else:
			return (str(r1)+"+"+str(i1*(-1))+"i")


