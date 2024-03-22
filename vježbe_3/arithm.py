import matplotlib.pyplot as plt
import numpy as np

#trebam izračunati aritmetičku sredinu i standardnu devijaciju za 10 točaka i proizvoljno ih uzimam (od 1 do 10 i 11 do 20 jer je najjednostavnije),uzimam dvije točke tj definiram dvije liste jer je dvodimenzionalni prostor
x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]

suma_x = sum(x)  #koristim funkciju sum za izračunati sumu svih elemenata u listama x i y
suma_y = sum(y)
arth_x= suma_x/len(x) #koristim funkciju arth za izračunavanje aritmetičke sredine tako da dijelim sumu s brojem elemenata u listi
arth_y = suma_y/len(y)
print (arth_x)
print (arth_y) 

#izračun st.dev. za listu x 
dev_x = 0 #definiram ovu varijablu za privremeno pohranjivanje standardne devijacije za listu x i tu trenutno izračunavam st.dev. unutar petlje
dev_x1 = [] #lista koja na kraju sadrži sve izračunate st.dev. za listu x, a svaka st.dev. koja se izračuna unutar petlje se doda u ovu listu za kasniju analizu

#dev_x je privremena, a dev_x1 je konačna varijabla tj lista
a = 0 #a je varijabla u koju dodajem izračunatu kvadratnu razliku za svaki element i aritm.sredinu

#započinjem for petlju koja prolazi kroz svaki element u listi x, svaki element predstavlja jedan od elemenata u listi x
n=10
for element in x:
    a += ((element - arth_x)**2) / n*(n-1) #ova naredba izračunava kvadratnu razliku trenutnog elementa i aritmetičke sredine arth_X i onda dijeli taj rezultat s n* ... i onda ga dodaje u varijablu a
    dev_x = np.sqrt(a)  #ova naredba izračunava kvadratni korijen izračunate sume kvadrata razlike; izračun standardne devijacije za trenutnu točku element u listi x
    dev_x1 .append (dev_x) #ova naredba dodaje izračunatu st.dev. dev_x u listu dev_x1 i svaka izračunata st.dev. se dodaje u ovu listu za kasnije korištenje
print(dev_x1) 
    
#ponavljam istu stvar za y listu
dev_y = 0
dev_y1 = []
b = 0
for element in y:
    b += ((element - arth_y)**2) / n*(n-1)
    dev_y = np.sqrt(b)
    dev_y1.append (dev_y)
print(dev_y1)

plt.scatter(dev_x1, dev_y1) #raspršenost po grafu
plt.show()