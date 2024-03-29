def iteracija(broj):
    x = 5 
    for i in range(broj): 
        x += (1/3)
    for i in range(broj): 
        x -= (1/3)
    print(x)

iteracija(200)
iteracija(2000)
iteracija(20000)