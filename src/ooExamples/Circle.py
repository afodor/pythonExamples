
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
		

c = Circle(5)
c.getArea()
c.getRadius()
