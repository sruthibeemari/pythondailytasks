import math
class Circle:
    def area (self,r):
        return math.pi*r*r
class Rectangle:
    def area(self,len,width):
        return len*width
class Triangle:
    def area(self,base,height):
        return 0.5*base*height
    
c=Circle()
r=Rectangle()
t=Triangle()

print("Area of Cirle: ",c.area(5))
print( "Area of Rectangle: ",r.area(5,8))
print("Area of Triangle: ",t.area(6,4))