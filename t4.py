import turtle

class Bentuk:
    def __init__(self):
        self.pen = turtle.Turtle()

    def buat_persegi(self, ukuran):
        for _ in range(4):
            self.pen.forward(ukuran)  
            self.pen.right(90)        

bentuk = Bentuk()

ukuran_sisi = 100

bentuk.buat_persegi(ukuran_sisi)

turtle.done()

