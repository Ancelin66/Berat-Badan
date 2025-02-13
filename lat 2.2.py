def hitung(x):
    if x == 0:
        return
    return (2 * x**3 + 2 * x + 15) / x

x = int(input("Masukkan bilangan bulat : "))

hasil = hitung(x)
print(f"Hasil dari f({x}) adalah {hasil}")
