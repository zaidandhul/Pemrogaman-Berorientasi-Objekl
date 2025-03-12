import turtle

class Turtlecees:
    def __init__(self, color, shape):
        self.tc = turtle.Turtle()  
        self.tc.color(color)  
        self.tc.shape(shape)  

    def maju(self, jarak):
        self.tc.forward(jarak)  

    def putar_kiri(self, sudut):
        self.tc.left(sudut)

    def buat_segitiga(self, ukuran):
        for _ in range(3):
            self.maju(ukuran)  
            self.putar_kiri(120) 
    def selesai(self):
        turtle.done()  

turtle1 = Turtlecees("brown", "classic")


turtle1.buat_segitiga(350)


turtle1.selesai()
