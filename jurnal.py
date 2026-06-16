from koleksi import Koleksi

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, penulis, volume, nomor_edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.penulis = penulis
        self.volume = volume
        self.nomor_edisi = nomor_edisi

    def tampilkan_data(self, nomor):
        return (
            f"Koleksi {nomor}   : [Jurnal]\n"
            f"Kode Koleksi      : {self.kode}\n"
            f"Judul             : {self.judul}\n"
            f"Tahun Rilis       : {self.tahun}\n"
            f"Penulis           : {self.penulis}\n"
            f"Volume            : {self.volume}\n"
            f"Nomor Edisi       : {self.nomor_edisi}\n"
            f"Penerbit          : {self.penerbit}\n"
        )
