class circle:
    def __init__(self , radius ):
        self.radius = radius
    def erea(self):
        return 3.14 * (self.radius ** 2)
    def circumference(self):
        return 2 * 3.14 * self.radius
radius = float(input("Enter a radius : " ))
circle = circle(radius)
print("The erea is : " , circle.erea())
print("The circumference is : " , circle.circumference())