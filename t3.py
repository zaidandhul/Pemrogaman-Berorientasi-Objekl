class LabMI:
    def __init__(self, nama_barang, kode_barang, jumlah_barang, kondisi_barang):
        self.nama_barang = nama_barang
        self.kode_barang = kode_barang
        self.jumlah_barang = jumlah_barang
        self.kondisi_barang = kondisi_barang

    def informasi_barang(self):

        print(f"Nama Barang     : {self.nama_barang}")
        print(f"Kode Barang     : {self.kode_barang}")
        print(f"Jumlah Barang   : {self.jumlah_barang}")
        print(f"Kondisi Barang  : {self.kondisi_barang}")

barang1 = LabMI ("Laptop", "AB101", "45", "Baik")

barang1.informasi_barang()