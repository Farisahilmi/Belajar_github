print("penambahan = 1\npengurangan = 2\nperkalian = 3\npembagian = 4\n")
masukan = int(input("pilih menu:"))
print("===== silahkan masukan nilai =====")
x = int(input("masukan nilai a:"))
y = int(input("masukan nilai b:"))


if masukan == 1:
    print(x + y)
elif masukan == 2:
    print(x - y)
elif masukan == 3:
    print(x * y)
elif masukan == 4:
    print(x // y)
else:
    print("error")

