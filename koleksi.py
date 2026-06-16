from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode       = kode
        self.judul      = judul
        self.tahun      = tahun
        self.penerbit   = penerbit
        self.status     = True # True =tersedia, False =dipinjam
    
    @abstractmethod
    def tampilkan_data(self, nomor):
        pass
