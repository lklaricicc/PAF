import math

def aritmeticka_sredina(tocke):
    return sum(tocke) / len(tocke)

def standardna_devijacija(tocke, srednja_vrijednost):
    suma_kvadrata_odstupanja = sum((x - srednja_vrijednost) ** 2 for x in tocke)
    varijanca = suma_kvadrata_odstupanja / len(tocke)
    return math.sqrt(varijanca)

# Unos točaka
tocke = []
for i in range(10):
    tocka = float(input(f"Unesite {i+1}. točku: "))
    tocke.append(tocka)

# Računanje aritmetičke sredine
sredina = aritmeticka_sredina(tocke)

# Računanje standardne devijacije
devijacija = standardna_devijacija(tocke, sredina)

# Ispis rezultata
print("Aritmetička sredina:", sredina)
print("Standardna devijacija:", devijacija)
