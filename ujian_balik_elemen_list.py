# Fungsi untuk membalik urutan dalam list

def balikPosisi(x):
    list_awal = x
    list_baru = []
    for i in range(len(list_awal)):
        list_baru.append(list_awal[len(list_awal)-1-i])
    return list_baru

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))