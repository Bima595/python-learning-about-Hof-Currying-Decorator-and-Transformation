def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Hof fungsi dalam fungsi
kali_dua = perkalian(2)
result = kali_dua(11)
print(result)

# currying percabangan variable 
kali_dua = perkalian(3)
hasil = kali_dua(95)
print(hasil)
