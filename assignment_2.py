jumlah_uang = int(input("Jumlah uang mu berapa:"))
total_belanja = int(input("total belanjaan mu berapa:"))

kembalian = jumlah_uang - total_belanja

if kembalian < 0:
    print("uangmu kurang")
else:
    print("kembalian:", kembalian)