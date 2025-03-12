import turtle

class Lingkaran:
    def __init__(self, radius):
        self.pen = turtle.Turtle()  
        self.radius = radius         
    
    def buat_lingkaran(self):
        self.pen.circle(self.radius)  

radius_lingkaran = 100

lingkaran = Lingkaran(radius_lingkaran)

lingkaran.buat_lingkaran()

turtle.done()

