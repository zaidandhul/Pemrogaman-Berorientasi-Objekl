import turtle

class GambarTurtle:
    def __init__(self):
        self.pen = turtle.Turtle()  

    def buat_segi_sembilan(self, ukuran):
        for _ in range(9):  
            self.pen.forward(ukuran)  
            self.pen.right(40)        

gambar = GambarTurtle()

ukuran_sisi = 90

gambar.buat_segi_sembilan(ukuran_sisi)

turtle.done()
