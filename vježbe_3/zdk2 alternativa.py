def iteracija(broj):
    x = 5 # definiram broj od kojeg oduzimam i zbrajam
    for i in range(broj): # za svaki broj u nizu, dodajem 1/3 broju 5 odnosno a
        x += (1/3)
    for i in range(broj): #za svaki broj u nizu oduzimam 1/3 broju 5
        x -= (1/3)
    print(x)

iteracija(200)
iteracija(2000)
iteracija(20000)
