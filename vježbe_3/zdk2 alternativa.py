def iteracija(broj):
    x = 5 # definiram varijablu od kojeg oduzimam i zbrajam 1/3
    for i in range(broj): # za svaki broj u nizu dodajem 1/3 broju 5 odnosno varijabli 
        x += (1/3)
    for i in range(broj): #za svaki broj u nizu oduzimam 1/3 
        x -= (1/3)
    print(x)

iteracija(200)
iteracija(2000)
iteracija(20000)

#u ovom kodu rezultat se ispisuje direktno u funkciju "iteracija(broj)", a konačni rezultat ispisuje direktno bez naredbe return (koristim samo jednu funkciju)
