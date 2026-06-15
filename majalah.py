from koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi, kategori):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi = edisi
        self.kategori = kategori

    def tampilkan_data(self, nomor):
        return (
            f"Koleksi {nomor}   : [Majalah]\n"
            f"Kode Koleksi      : {self.kode}\n"
            f"Judul             : {self.judul}\n"
            f"Tahun Rilis       : {self.tahun}\n"
            f"Edisi             : {self.edisi}\n"
            f"Kategori          : {self.kategori}\n"
            f"Penerbit          : {self.penerbit}\n"
        )
