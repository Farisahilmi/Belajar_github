harga_dasar = 2500000
harga_jual  = 3000000

jumlah_domba = int("jumlah domba yang dijual: ")

total_modal = harga_dasar * jumlah_domba
total_penjualan = harga_jual * jumlah_domba
keuntungan = total_penjualan - total_modal

print("total modal:", total_modal)
print("total keuntungan", keuntungan)
