from buku import Buku
from majalah import Majalah
from jurnal import Jurnal
from dvd import DVD


class Perpustakaan:
    INPUT_WIDTH = 15

    def __init__(self):
        self.daftar_koleksi = []

        self.jenis_koleksi = {
            "1": {
                "nama": "Buku",
                "class": Buku,
                "fields": [
                    ("pengarang", "Pengarang"),
                    ("jumlah_halaman", "Jumlah Halaman"),
                    ("sinopsis", "Sinopsis")
                ]
            },
            "2": {
                "nama": "Majalah",
                "class": Majalah,
                "fields": [
                    ("edisi", "Edisi"),
                    ("kategori", "Kategori")
                ]
            },
            "3": {
                "nama": "Jurnal",
                "class": Jurnal,
                "fields": [
                    ("penulis", "Penulis"),
                    ("volume", "Volume"),
                    ("nomor_edisi", "Nomor Edisi")
                ]
            },
            "4": {
                "nama": "DVD Film Dokumenter",
                "class": DVD,
                "fields": [
                    ("sutradara", "Sutradara"),
                    ("bidang_ilmu", "Bidang Ilmu"),
                    ("durasi", "Durasi (menit)")
                ]
            }
        }

    def tambah_koleksi(self):
        print("\n===== Tambah Koleksi =====")

        for key, value in self.jenis_koleksi.items():
            print(f"{key}. {value['nama']}")

        pilihan = input("Pilih jenis koleksi : ")

        if pilihan not in self.jenis_koleksi:
            print("Pilihan tidak valid.")
            return

        data = self.jenis_koleksi[pilihan]

        kode = input(f"{'Kode Koleksi':<{self.INPUT_WIDTH}} : ")
        judul = input(f"{'Judul':<{self.INPUT_WIDTH}} : ")
        tahun = input(f"{'Tahun Rilis':<{self.INPUT_WIDTH}} : ")
        penerbit = input(f"{'Penerbit':<{self.INPUT_WIDTH}} : ")

        atribut_tambahan = []

        for _, label in data["fields"]:
            atribut_tambahan.append(input(f"{label:<{self.INPUT_WIDTH}} : "))

        koleksi = data["class"](
            kode,
            judul,
            tahun,
            penerbit,
            *atribut_tambahan
        )

        self.daftar_koleksi.append(koleksi)

        print("\nData berhasil ditambahkan.")

    def hapus_koleksi(self):
        kode = input("\nMasukkan kode koleksi: ")

        for koleksi in self.daftar_koleksi:
            if koleksi.kode == kode:
                self.daftar_koleksi.remove(koleksi)
                print("Data berhasil dihapus.")
                return

        print("Data tidak ditemukan.")

    def tampilkan_semua(self):
        if not self.daftar_koleksi:
            print("\nBelum ada data koleksi.")
            return

        print("\n===== Daftar Koleksi =====\n")

        for nomor, koleksi in enumerate(self.daftar_koleksi, start=1):
            print(koleksi.tampilkan_data(nomor))
            print("-" * 50)

    def menu(self):
        while True:
            print("\n===== SISTEM PERPUSTAKAAN =====")
            print("1. Tambah koleksi")
            print("2. Hapus koleksi")
            print("3. Tampilkan semua koleksi")
            print("4. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tambah_koleksi()

            elif pilihan == "2":
                self.hapus_koleksi()

            elif pilihan == "3":
                self.tampilkan_semua()

            elif pilihan == "4":
                print("Program selesai.")
                break

            else:
                print("Menu tidak tersedia.")