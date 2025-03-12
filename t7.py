import turtle

class Bintang:
    def __init__(self, turtle_obj, ukuran):
        self.pen = turtle_obj  
        self.ukuran = ukuran   
    
    def buat_bintang(self):
        for _ in range(5):
            self.pen.forward(self.ukuran)
            self.pen.right(144)

layar = turtle.Screen()

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.speed(3)
pen2.speed(3)

pen1.penup()
pen1.goto(-150, 0) 
pen1.pendown()

pen2.penup()
pen2.goto(150, 0)  
pen2.pendown()

ukuran_bintang = 100
bintang1 = Bintang(pen1, ukuran_bintang)
bintang2 = Bintang(pen2, ukuran_bintang)

bintang1.buat_bintang()
bintang2.buat_bintang()

layar.exitonclick()
