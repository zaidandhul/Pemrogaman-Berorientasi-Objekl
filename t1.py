class Mahasiswa:
  
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    def tampilkan_data(self):
    
        print(f"Nama       : {self.nama}")
        print(f"Kelas      : {self.kelas}")
        print(f"NIM        : {self.nim}")
        print(f"Jurusan    : {self.jurusan}")
        print(f"Fakultas   : {self.fakultas}")
        print(f"Kampus     : {self.kampus}")

mahasiswa1 = Mahasiswa(
    nama="Zaidan Dhiya Ulhaq",
    kelas="2023E",
    nim="23091397152",
    jurusan="Manajemen Informatika",
    fakultas="Fakultas Vokasi",
    kampus="Universitas Negeri Surabaya")

mahasiswa1.tampilkan_data()
