from koleksi import Koleksi

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, pengarang, jumlah_halaman, sinopsis):
        super().__init__(kode, judul, tahun, penerbit)
        self.pengarang       = pengarang
        self.jumlah_halaman  = jumlah_halaman
        self.sinopsis        = sinopsis

    def tampilkan_data(self,  nomor):
        return(
            f"Koleksi {nomor}   : [Buku]\n"
            f"Kode Koleksi      : {self.kode}\n"
            f"Judul             : {self.judul}\n"
            f"Tahun Rilis       : {self.tahun}\n"
            f"Pengarang         : {self.pengarang}\n"
            f"Jumlah Halaman    : {self.jumlah_halaman} halaman\n"
            f"Sinopsis          : {self.sinopsis}\n"
            f"Penerbit          : {self.penerbit}\n"
        )