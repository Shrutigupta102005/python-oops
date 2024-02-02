class circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        area=(22/7)*self.r*self.r
        print(f"Area of circle is{area}")

    def perimeter(self):
        perimeter=2*(22/7)*self.r
        print(f"perimeter of circle is{perimeter}")

class rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        area=self.a*self.b
        print(f"Area of rect is{area}")

    def perimeter(self):
        perimeter=2*(self.a+self.b)
        print(f"perimeter of rectangle is{perimeter}")
    
class triangle:
    def __init__(self,s1,s2,s3):
        self.s1=s1 #(base)
        self.s2=s2 #(height)
        self.s3=s3
    def area(self):
        area=1/2*self.s1*self.s2
        print(f"Area of triangle is{area}")

    def perimeter(self):
        perimeter=self.s1+self.s2+self.s3
        print(f"perimeter of triangle is{perimeter}")
