def hitung_berat_badan(tinggi, bmi_diinginkan):
    berat_diperlukan = bmi_diinginkan * (tinggi ** 2)
    return berat_diperlukan

tinggi = float(input("Masukkan tinggi badan (m): "))
bmi_diinginkan = float(input("Masukkan BMI yang diinginkan: "))

berat_diperlukan = hitung_berat_badan(tinggi, bmi_diinginkan)

print(f"Berat badan yang diperlukan untuk BMI yang diinginkan {bmi_diinginkan} dengan tinggi {tinggi} m adalah {berat_diperlukan:.2f} kg")
