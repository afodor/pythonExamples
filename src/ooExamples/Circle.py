
import math

class Circle:	
	
	def __init__(self,radius):
		self.radius = radius
	
	def setRadius(self, radius):
		self.radius = radius
	
	def getRadius(self):
		return self.radius;
	
	def getArea(self):
		return math.pi * self.radius ** 2
		

c1 = Circle(5)
c1.getArea()
c1.getRadius()

c2 = Circle(6)
c2.getArea()
c2.getRadius()

