from koleksi import Koleksi

class DVD(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_ilmu, sutradara, durasi):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang_ilmu = bidang_ilmu
        self.sutradara   = sutradara
        self.durasi      = durasi

    def tampilkan_data(self,  nomor):
        return(
            f"Koleksi {nomor}   : [DVD Film Dokumenter]\n"
            f"Kode Koleksi      : {self.kode}\n"
            f"Judul             : {self.judul}\n"
            f"Tahun Rilis       : {self.tahun}\n"
            f"Bidang Ilmu       : {self.bidang_ilmu}\n"
            f"Sutradara         : {self.sutradara}\n"
            f"Durasi            : {self.durasi} menit\n"
            f"Distributor       : {self.penerbit}\n"
        )