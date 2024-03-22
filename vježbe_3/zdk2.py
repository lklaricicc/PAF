def iteracija (N):
    x=5 
    for i in range (N):
        x +=1/3
    for i in range (N): 
        x -= 1/3
    x -= 5
    return x 
        
for N in [200,2000,20000]:
    konacni_rezultat = iteracija(N)
    print("Za" ,N, "interacija", "rezultat je:" , konacni_rezultat)

#očekivan rezultat je 0 jer smo definirali 
#vrijednost rezultat=0 i jer N puta dodajemo 1/ i oduzimamo 1/3,
#mislim kako ovdje opet ulogu igra računanje s decimalnim brojevima i
#to što ne koristimo naredbu float