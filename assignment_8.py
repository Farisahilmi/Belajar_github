a = float(input("masukan alas: "))
t = float(input("masukan tinggi: "))

luas = 0.5 * a * t
sisi_miring = (a**2 + t**2) ** 0.5
keliling = a + t + sisi_miring
print(f"luas : {luas}, keliling: {keliling}")