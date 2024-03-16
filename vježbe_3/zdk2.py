def izracunaj_rezultat (N):
    rezultat = 0
    for i in range (N):
        rezultat +=1/3
    for i in range (N): 
        rezultat -= 1/3
    rezultat -= 5
    return rezultat 
        
for N in [200,2000,20000]:
    konacni_rezultat = izracunaj_rezultat(N)
    print("Za" ,N, "interacija", "rezultat je:" , konacni_rezultat)
