from buku import Buku
from majalah import Majalah
from jurnal import Jurnal


class Perpustakaan:
    def __init__(self):
        self.daftar_koleksi = []

    def tambah_koleksi(self):
        print("\n===== Tambah Koleksi =====")
        print("1. Buku")
        print("2. Majalah")
        print("3. Jurnal")

        pilihan = input("Pilih jenis koleksi: ")

        kode = input("Kode koleksi    : ")
        judul = input("Judul           : ")
        tahun = input("Tahun terbit    : ")

        if pilihan == "1":
            pengarang = input("Pengarang       : ")
            penerbit = input("Penerbit        : ")

            koleksi = Buku(
                kode,
                judul,
                tahun,
                pengarang,
                penerbit
            )

        elif pilihan == "2":
            penerbit = input("Penerbit        : ")
            edisi = input("Edisi           : ")

            koleksi = Majalah(
                kode,
                judul,
                tahun,
                penerbit,
                edisi
            )

        elif pilihan == "3":
            penerbit = input("Penerbit        : ")
            bidang = input("Bidang studi    : ")
            impact = input("Impact factor   : ")

            koleksi = Jurnal(
                kode,
                judul,
                tahun,
                penerbit,
                bidang,
                impact
            )

        else:
            print("Pilihan tidak valid.")
            return

        self.daftar_koleksi.append(koleksi)
        print("\nData berhasil ditambahkan.")

    def hapus_koleksi(self):
        kode = input("\nMasukkan kode koleksi: ")

        for koleksi in self.daftar_koleksi:
            if koleksi.kode_koleksi == kode:
                self.daftar_koleksi.remove(koleksi)
                print("Data berhasil dihapus.")
                return

        print("Data tidak ditemukan.")

    def tampilkan_semua(self):
        if not self.daftar_koleksi:
            print("\nBelum ada data koleksi.")
            return

        print("\n===== Daftar Koleksi =====")

        for nomor, koleksi in enumerate(self.daftar_koleksi, start=1):
            print(f"\nKoleksi ke-{nomor}")
            koleksi.tampilkan_data()
            print("-" * 30)

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