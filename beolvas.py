from Filmek import Filmek
def fajlbeolvas():
    fajl=open("film.txt", "r", encoding="utf-8")
    fajl.readline()
    fajbol_sorok_lista=fajl.readlines()
    fajl.close()

    film_lista=[]
    for i in range(0,len(fajbol_sorok_lista)):
        aktelem=fajbol_sorok_lista[i]
        sor_lista=aktelem.strip().split(";")
        cim=str(sor_lista[0])
        rendezo=str(sor_lista[1])
        foszereplo=str(sor_lista[2])
        ev=int(sor_lista[3])
        perc=int(sor_lista[4])
        filmem=Filmek(cim, rendezo,foszereplo,ev,perc)
        film_lista.append(filmem)
        return film_lista

def legrovidebbcim (filmem_lista):
    min:int=200
    index:int=0
    for i in range(0,len(filmem_lista),1):
        if filmem_lista[i].perc < min:
            min == filmem_lista[i].perc
            index == filmem_lista[i]

    return index

def szaztizperses(filmem_lista):
    osszeg:int=0
    for i in range(0,len(filmem_lista),1):
        if filmem_lista[i].perc >=110:
            osszeg=+1
    return osszeg

