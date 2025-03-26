from datetime import datetime
import math

pengeluaran = []
while True:
    print("\n=== Pencatatan Pengeluaran ===")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Pengeluaran")
    print("3. Hapus Pengeluaran")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        kategori = input("Kategori (Makanan, Transportasi, dll): ")
        jumlah = float(input("Jumlah (Rp): "))
        pengeluaran.append([tanggal, kategori, jumlah])
        print("Pengeluaran ditambahkan!")
        total = math.fsum(p[2] for p in pengeluaran)
        print(f"\nTotal Pengeluaran Sekarang: Rp{total:,.2f}")

    elif pilihan == "2":
        if not pengeluaran:
            print("Belum ada pengeluaran.")
        else:
            print("\n=== Daftar Pengeluaran ===")
            print("No | Tanggal             | Kategori        | Jumlah (Rp)")
            print("-" * 60)
            for i, p in enumerate(pengeluaran, 1):
                print(f"{i}  | {p[0]} | {p[1]:<15} | Rp{p[2]:,.2f}")

    elif pilihan == "3":
        if not pengeluaran:
            print("Belum ada pengeluaran.")
        else:
            print("\n=== Daftar Pengeluaran ===")
            for i, p in enumerate(pengeluaran, 1):
                print(f"{i}. {p[0]} | {p[1]} - Rp{p[2]:,.2f}")

            try:
                index = int(input("Pilih nomor pengeluaran yang ingin dihapus: ")) - 1
                if 0 <= index < len(pengeluaran):
                    del pengeluaran[index]
                    print("Pengeluaran berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Masukkan angka yang benar.")

    elif pilihan == "4":
        print("Anda keluar dari program. Terima kasih!")
        break

    else:
        print("Tidak ada opsi yang sesuai. Silahkan coba lagi!")